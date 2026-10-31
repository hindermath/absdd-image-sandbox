using System.Diagnostics;
using System.Text;
using System.Text.Json;
using HomeBaseline.MaintenanceTui.Contracts;

namespace HomeBaseline.MaintenanceTui.Infrastructure;

public sealed record ProcessExecutionResult(
    int ExitCode,
    string StandardOutput,
    string StandardError,
    AtomicRunReport? Report = null,
    MaintenanceEvent? CompletionEvent = null,
    bool EventStreamDegraded = false);

public interface IMaintenanceProcessRunner
{
    Task<ProcessExecutionResult> RunAsync(
        ProcessInvocation invocation,
        CancellationToken cancellationToken);
}

public sealed class MaintenanceProcessRunner : IMaintenanceProcessRunner
{
    private sealed record EventReadOutcome(MaintenanceEvent? Completion, bool Degraded);
    private const int DiagnosticTailChars = 65536;
    private const int EventReadBytes = 4096;
    private const int MaximumReportBytes = 1024 * 1024;
    private readonly Action<MaintenanceEvent>? _eventSink;
    private readonly Action<EventReaderState>? _degradationSink;

    public MaintenanceProcessRunner(
        Action<MaintenanceEvent>? eventSink = null,
        Action<EventReaderState>? degradationSink = null)
    {
        _eventSink = eventSink;
        _degradationSink = degradationSink;
    }

    public async Task<ProcessExecutionResult> RunAsync(
        ProcessInvocation invocation,
        CancellationToken cancellationToken)
    {
        if (cancellationToken.IsCancellationRequested)
        {
            return new ProcessExecutionResult(130, string.Empty, string.Empty);
        }

        var startInfo = new ProcessStartInfo(invocation.Executable)
        {
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
        };
        foreach (var argument in invocation.Arguments)
        {
            startInfo.ArgumentList.Add(argument);
        }

        using var process = new Process { StartInfo = startInfo };
        if (!process.Start())
        {
            throw new InvalidOperationException("Maintenance process did not start.");
        }

        var stdout = ReadBoundedTailAsync(process.StandardOutput);
        var stderr = ReadBoundedTailAsync(process.StandardError);
        var eventTask = ReadEventsUntilExitAsync(process, invocation, CancellationToken.None);
        try
        {
            await process.WaitForExitAsync(cancellationToken);
        }
        catch (OperationCanceledException)
        {
            if (!process.HasExited)
            {
                // Der Wrapper erhaelt Ctrl+C bereits einmal ueber die gemeinsame Konsolengruppe.
                // The wrapper already receives Ctrl+C once through the shared console group.
                await process.WaitForExitAsync(CancellationToken.None);
            }

            var cancelledOutcome = await eventTask;
            var cancelledEvent = cancelledOutcome.Completion;
            var cancelledReport = ReadReport(
                cancelledEvent,
                invocation.ReportPath,
                invocation.RunId);
            return new ProcessExecutionResult(
                130,
                await stdout,
                await stderr,
                cancelledReport,
                cancelledEvent,
                cancelledOutcome.Degraded);
        }

        var outcome = await eventTask;
        var completionEvent = outcome.Completion;
        var report = ReadReport(
            completionEvent,
            invocation.ReportPath,
            invocation.RunId);
        return new ProcessExecutionResult(
            process.ExitCode,
            await stdout,
            await stderr,
            report,
            completionEvent,
            outcome.Degraded);
    }

    private async Task<EventReadOutcome> ReadEventsUntilExitAsync(
        Process process,
        ProcessInvocation invocation,
        CancellationToken cancellationToken)
    {
        var reader = new MaintenanceEventReader(invocation.RunId);
        var decoder = new UTF8Encoding(false, true).GetDecoder();
        MaintenanceEvent? completion = null;
        long offset = 0;
        while (!process.HasExited)
        {
            ReadNewContent(invocation.EventStreamPath, reader, decoder, ref completion, ref offset);
            await Task.Delay(LiveDelay, cancellationToken);
        }

        ReadNewContent(invocation.EventStreamPath, reader, decoder, ref completion, ref offset);
        var finalCharacters = new char[4];
        try
        {
            var finalCount = decoder.GetChars(
                Array.Empty<byte>(), 0, 0, finalCharacters, 0, flush: true);
            if (finalCount > 0)
            {
                reader.Feed(new string(finalCharacters, 0, finalCount));
            }
        }
        catch (DecoderFallbackException)
        {
            reader.Feed("{invalid utf-8}\n");
        }
        var beforeComplete = reader.State.PresentationMode;
        reader.Complete();
        if (beforeComplete != EventPresentationMode.Degraded &&
            reader.State.PresentationMode == EventPresentationMode.Degraded)
        {
            _degradationSink?.Invoke(reader.State);
        }
        var degraded = reader.State.PresentationMode == EventPresentationMode.Degraded;
        return new EventReadOutcome(degraded ? null : completion, degraded);
    }

    private static readonly TimeSpan LiveDelay = TimeSpan.FromMilliseconds(100);

    private void ReadNewContent(
        string path,
        MaintenanceEventReader reader,
        Decoder decoder,
        ref MaintenanceEvent? completion,
        ref long offset)
    {
        if (!File.Exists(path))
        {
            return;
        }

        using var stream = new FileStream(
            path,
            FileMode.Open,
            FileAccess.Read,
            FileShare.ReadWrite | FileShare.Delete);
        if (stream.Length <= offset)
        {
            return;
        }

        stream.Position = offset;
        var previousMode = reader.State.PresentationMode;
        var bytes = new byte[EventReadBytes];
        var characters = new char[EventReadBytes];
        int read;
        while ((read = stream.Read(bytes, 0, bytes.Length)) > 0)
        {
            offset += read;
            int decoded;
            try
            {
                decoded = decoder.GetChars(bytes, 0, read, characters, 0, flush: false);
            }
            catch (DecoderFallbackException)
            {
                reader.Feed("{invalid utf-8}\n");
                break;
            }
            foreach (var maintenanceEvent in reader.Feed(new string(characters, 0, decoded)))
            {
                if (maintenanceEvent.EventType == MaintenanceEventTypes.RunCompleted)
                {
                    completion = maintenanceEvent;
                }
                _eventSink?.Invoke(maintenanceEvent);
            }
        }
        if (previousMode != EventPresentationMode.Degraded &&
            reader.State.PresentationMode == EventPresentationMode.Degraded)
        {
            _degradationSink?.Invoke(reader.State);
        }
    }

    private static async Task<string> ReadBoundedTailAsync(StreamReader stream)
    {
        var tail = new StringBuilder();
        var buffer = new char[4096];
        var truncated = false;
        int read;
        while ((read = await stream.ReadAsync(buffer, 0, buffer.Length)) > 0)
        {
            tail.Append(buffer, 0, read);
            if (tail.Length > DiagnosticTailChars)
            {
                tail.Remove(0, tail.Length - DiagnosticTailChars);
                truncated = true;
            }
        }
        return truncated ? "[truncated]\n" + tail : tail.ToString();
    }

    private static AtomicRunReport? ReadReport(
        MaintenanceEvent? completionEvent,
        string expectedReportPath,
        Guid expectedRunId)
    {
        var reportPath = expectedReportPath;
        if (completionEvent is not null &&
            completionEvent.Details.TryGetProperty("reportPath", out var reportProperty) &&
            reportProperty.ValueKind == JsonValueKind.String)
        {
            var eventReportPath = reportProperty.GetString();
            if (!string.IsNullOrWhiteSpace(eventReportPath) &&
                PathsEqual(eventReportPath, expectedReportPath))
            {
                reportPath = eventReportPath;
            }
        }

        // Der vor Prozessstart gebundene Pfad verhindert eine racy Suche nach fremden Laufberichten.
        // The pre-bound path avoids a racy search that could select another run's report.
        if (string.IsNullOrWhiteSpace(reportPath) || !File.Exists(reportPath))
        {
            return null;
        }

        try
        {
            using var reportStream = new FileStream(
                reportPath, FileMode.Open, FileAccess.Read,
                FileShare.ReadWrite | FileShare.Delete);
            if (reportStream.Length > MaximumReportBytes)
            {
                return null;
            }
            var reportBytes = new byte[MaximumReportBytes + 1];
            var total = 0;
            int chunk;
            while (total < reportBytes.Length &&
                   (chunk = reportStream.Read(reportBytes, total, reportBytes.Length - total)) > 0)
            {
                total += chunk;
            }
            if (total > MaximumReportBytes)
            {
                return null;
            }
            using var document = JsonDocument.Parse(reportBytes.AsMemory(0, total));
            var root = document.RootElement;
            if (!root.TryGetProperty("runId", out var runProperty) ||
                !Guid.TryParse(runProperty.GetString(), out var runId) ||
                runId != expectedRunId ||
                !root.TryGetProperty("overallStatus", out var statusProperty) ||
                !root.TryGetProperty("exitCode", out var exitProperty))
            {
                return null;
            }

            var finalized = root.TryGetProperty("finalized", out var finalizedProperty) &&
                            finalizedProperty.ValueKind == JsonValueKind.True;
            var logPath = root.TryGetProperty("artifacts", out var artifacts) &&
                          artifacts.TryGetProperty("logPath", out var logProperty)
                ? logProperty.GetString() ?? "N/A"
                : "N/A";
            return new AtomicRunReport(
                reportPath,
                runId,
                finalized,
                statusProperty.GetString() ?? "UNKNOWN",
                exitProperty.GetInt32(),
                logPath,
                ReadDisplaySummary(root));
        }
        catch (Exception exception) when (
            exception is JsonException or
            IOException or
            UnauthorizedAccessException or
            InvalidOperationException)
        {
            return null;
        }
    }

    private static bool PathsEqual(string left, string right)
    {
        try
        {
            var comparison = OperatingSystem.IsWindows()
                ? StringComparison.OrdinalIgnoreCase
                : StringComparison.Ordinal;
            return string.Equals(
                Path.GetFullPath(left),
                Path.GetFullPath(right),
                comparison);
        }
        catch (Exception exception) when (
            exception is ArgumentException or
            IOException or
            NotSupportedException)
        {
            return false;
        }
    }

    private static RunDisplaySummary ReadDisplaySummary(JsonElement root)
    {
        var barrier = "UNKNOWN";
        if (root.TryGetProperty("mutationBarrier", out var mutationBarrier) &&
            mutationBarrier.ValueKind == JsonValueKind.Object &&
            mutationBarrier.TryGetProperty("fleetReady", out var fleetReady) &&
            fleetReady.ValueKind is JsonValueKind.True or JsonValueKind.False)
        {
            barrier = fleetReady.GetBoolean() ? "OPEN" : "BLOCKED";
        }

        var counts = root.TryGetProperty("counts", out var countObject) &&
                     countObject.ValueKind == JsonValueKind.Object
            ? countObject
            : default;
        var statusClasses = new Dictionary<string, int>(StringComparer.Ordinal);
        if (root.TryGetProperty("targets", out var targets) &&
            targets.ValueKind == JsonValueKind.Array)
        {
            foreach (var target in targets.EnumerateArray())
            {
                if (!target.TryGetProperty("status", out var status) ||
                    status.ValueKind != JsonValueKind.String)
                {
                    continue;
                }

                var name = status.GetString() ?? "UNKNOWN";
                statusClasses[name] = statusClasses.GetValueOrDefault(name) + 1;
            }
        }

        return new RunDisplaySummary(
            barrier,
            Count(counts, "targets"),
            Count(counts, "passed"),
            Count(counts, "warnings"),
            Count(counts, "blocked"),
            Count(counts, "failed"),
            statusClasses,
            "Nicht separat berichtet / not separately reported",
            StageStatus(root, "preset-profiles"),
            LastNextAction(root));
    }

    private static int Count(JsonElement counts, string name) =>
        counts.ValueKind == JsonValueKind.Object &&
        counts.TryGetProperty(name, out var value) &&
        value.ValueKind == JsonValueKind.Number &&
        value.TryGetInt32(out var result)
            ? result
            : 0;

    private static string StageStatus(JsonElement root, string stageId)
    {
        if (!root.TryGetProperty("stages", out var stages) ||
            stages.ValueKind != JsonValueKind.Array)
        {
            return "UNKNOWN";
        }

        foreach (var stage in stages.EnumerateArray())
        {
            if (stage.TryGetProperty("stageId", out var id) &&
                string.Equals(id.GetString(), stageId, StringComparison.Ordinal) &&
                stage.TryGetProperty("status", out var status) &&
                status.ValueKind == JsonValueKind.String)
            {
                return status.GetString() ?? "UNKNOWN";
            }
        }

        return "UNKNOWN";
    }

    private static string LastNextAction(JsonElement root)
    {
        if (root.TryGetProperty("mutationBarrier", out var barrier) &&
            barrier.ValueKind == JsonValueKind.Object &&
            barrier.TryGetProperty("nextAction", out var barrierAction) &&
            barrierAction.ValueKind == JsonValueKind.String &&
            !string.Equals(barrierAction.GetString(), "N/A", StringComparison.Ordinal))
        {
            return barrierAction.GetString() ?? "N/A";
        }

        if (!root.TryGetProperty("stages", out var stages) ||
            stages.ValueKind != JsonValueKind.Array)
        {
            return "N/A";
        }

        foreach (var stage in stages.EnumerateArray().Reverse())
        {
            if (stage.TryGetProperty("nextAction", out var action) &&
                action.ValueKind == JsonValueKind.String &&
                !string.IsNullOrWhiteSpace(action.GetString()))
            {
                return action.GetString() ?? "N/A";
            }
        }

        return "N/A";
    }

}
