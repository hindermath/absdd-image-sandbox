using HomeBaseline.MaintenanceTui.Application;
using HomeBaseline.MaintenanceTui.Infrastructure;
using HomeBaseline.MaintenanceTui.Tests.Contracts;

namespace HomeBaseline.MaintenanceTui.Tests.Integration;

[TestClass]
public sealed class BoundedProcessOutputTests
{
    [TestMethod]
    public async Task IncompleteUtf8TailCannotKeepCompletionEvent()
    {
        if (OperatingSystem.IsWindows()) return;

        var runId = Guid.NewGuid();
        var path = Path.Combine(Path.GetTempPath(), runId + ".events.jsonl");
        var reportPath = Path.Combine(Path.GetTempPath(), runId + ".report.json");
        try
        {
            var completed = MaintenanceEventTests.EventJson(
                runId, 1, "run-completed", "SUCCESS") + "\n";
            var bytes = System.Text.Encoding.UTF8.GetBytes(completed);
            await File.WriteAllBytesAsync(path, [.. bytes, 0xC3]);
            await File.WriteAllTextAsync(reportPath,
                System.Text.Json.JsonSerializer.Serialize(new {
                    runId, overallStatus = "PASSED", exitCode = 0, finalized = true
                }));
            var invocation = new ProcessInvocation(
                "/bin/sh", ["-c", "true"], "synthetic completion fixture",
                path, reportPath, runId);
            var degradationNotified = false;
            var runner = new MaintenanceProcessRunner(
                degradationSink: _ => degradationNotified = true);
            var execution = await runner.RunAsync(
                invocation, CancellationToken.None);
            var result = await new MaintenanceTuiApplication(
                runner, new RunResultReconciler()).ExecuteAsync(
                    invocation, CancellationToken.None);

            Assert.AreEqual(0, execution.ExitCode);
            Assert.IsNull(execution.CompletionEvent);
            Assert.IsTrue(execution.EventStreamDegraded);
            Assert.IsTrue(degradationNotified);
            Assert.AreEqual("RESULT_MISMATCH", result.DisplayStatus);
            Assert.AreEqual(0, result.ProcessExitCode);
        }
        finally
        {
            File.Delete(path);
            File.Delete(reportPath);
        }
    }

    [TestMethod]
    public async Task LargeChildPipesAreDrainedWithBoundedDiagnosticTails()
    {
        if (OperatingSystem.IsWindows()) return;

        var runId = Guid.NewGuid();
        var invocation = new ProcessInvocation(
            "/bin/sh",
            ["-c", "i=0; while [ $i -lt 5000 ]; do printf 'stdout-0123456789\\n'; printf 'stderr-0123456789\\n' >&2; i=$((i+1)); done"],
            "synthetic output fixture",
            Path.Combine(Path.GetTempPath(), runId + ".events.jsonl"),
            Path.Combine(Path.GetTempPath(), runId + ".report.json"),
            runId);

        var result = await new MaintenanceProcessRunner().RunAsync(
            invocation, CancellationToken.None);

        Assert.AreEqual(0, result.ExitCode);
        Assert.IsTrue(result.StandardOutput.StartsWith("[truncated]\n"));
        Assert.IsTrue(result.StandardError.StartsWith("[truncated]\n"));
        Assert.IsTrue(result.StandardOutput.Length <= 65549);
        Assert.IsTrue(result.StandardError.Length <= 65549);
    }
}
