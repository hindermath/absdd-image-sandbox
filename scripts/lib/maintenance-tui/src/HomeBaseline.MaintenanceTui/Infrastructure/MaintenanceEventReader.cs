using System.Text;
using System.Text.Json;
using HomeBaseline.MaintenanceTui.Contracts;

namespace HomeBaseline.MaintenanceTui.Infrastructure;

public sealed class MaintenanceEventReader
{
    private const int MaximumRecordChars = 65536;
    private static readonly HashSet<string> AllowedProperties = new(StringComparer.Ordinal)
    {
        "schemaVersion",
        "runId",
        "sequence",
        "timestampUtc",
        "eventType",
        "status",
        "phaseId",
        "targetId",
        "messageDe",
        "messageEn",
        "details",
    };

    private readonly Guid _runId;
    private readonly StringBuilder _pending = new();
    private bool _discardOversizedRecord;
    private long _byteOffset;
    private long _expectedSequence = 1;
    private EventPresentationMode _presentationMode = EventPresentationMode.Enhanced;
    private EventDegradationReason _degradationReason;
    private MaintenanceEvent? _lastEvent;

    public MaintenanceEventReader(Guid runId)
    {
        _runId = runId;
    }

    public EventReaderState State =>
        new(_byteOffset, _expectedSequence, _presentationMode, _degradationReason, _lastEvent);

    public IReadOnlyList<MaintenanceEvent> Feed(string content)
    {
        if (string.IsNullOrEmpty(content))
        {
            return [];
        }

        var records = new List<MaintenanceEvent>();
        foreach (var character in content)
        {
            if (_discardOversizedRecord)
            {
                if (character == '\n')
                {
                    _discardOversizedRecord = false;
                }
                continue;
            }
            if (character == '\n')
            {
                var line = _pending.ToString().TrimEnd('\r');
                _pending.Clear();
                if (line.Length == 0)
                {
                    Degrade(EventDegradationReason.InvalidSchema);
                    continue;
                }
                var parsed = Parse(line);
                if (parsed is not null)
                {
                    records.Add(parsed);
                }
                continue;
            }
            if (_pending.Length >= MaximumRecordChars)
            {
                // Drop through the next newline; a later completion cannot
                // silently repair a missing middle event.
                _pending.Clear();
                _discardOversizedRecord = true;
                Degrade(EventDegradationReason.OversizedRecord);
                continue;
            }
            _pending.Append(character);
        }
        _byteOffset += Encoding.UTF8.GetByteCount(content);

        return records;
    }

    public void Complete()
    {
        if (_discardOversizedRecord || _pending.Length > 0)
        {
            _pending.Clear();
            _discardOversizedRecord = false;
            Degrade(EventDegradationReason.InvalidSchema);
        }
    }

    private MaintenanceEvent? Parse(string line)
    {
        try
        {
            using var document = JsonDocument.Parse(line);
            if (document.RootElement.ValueKind != JsonValueKind.Object)
            {
                return DegradeAndReturn(EventDegradationReason.InvalidSchema);
            }

            foreach (var property in document.RootElement.EnumerateObject())
            {
                if (!AllowedProperties.Contains(property.Name))
                {
                    return DegradeAndReturn(EventDegradationReason.InvalidSchema);
                }
            }

            if (!TryGetRequiredValues(document.RootElement, out var parsed))
            {
                return DegradeAndReturn(EventDegradationReason.InvalidSchema);
            }

            if (parsed.RunId != _runId)
            {
                return DegradeAndReturn(EventDegradationReason.RunMismatch);
            }

            if (parsed.Sequence != _expectedSequence)
            {
                return DegradeAndReturn(EventDegradationReason.SequenceGap);
            }

            _expectedSequence++;
            _lastEvent = parsed;
            return parsed;
        }
        catch (JsonException)
        {
            return DegradeAndReturn(EventDegradationReason.InvalidJson);
        }
    }

    private static bool TryGetRequiredValues(JsonElement root, out MaintenanceEvent value)
    {
        value = null!;
        if (!TryGetInt32(root, "schemaVersion", out var schemaVersion) || schemaVersion != 1 ||
            !TryGetGuid(root, "runId", out var runId) ||
            !TryGetInt64(root, "sequence", out var sequence) || sequence < 1 ||
            !TryGetText(root, "timestampUtc", out var timestampText) ||
            !DateTimeOffset.TryParse(timestampText, out var timestamp) ||
            !timestampText.EndsWith('Z') ||
            !TryGetText(root, "eventType", out var eventType) ||
            !MaintenanceEventTypes.All.Contains(eventType) ||
            !TryGetText(root, "status", out var status) ||
            !MaintenanceStatuses.All.Contains(status) ||
            !TryGetText(root, "messageDe", out var messageDe) ||
            !TryGetText(root, "messageEn", out var messageEn) ||
            !root.TryGetProperty("details", out var details) ||
            details.ValueKind != JsonValueKind.Object)
        {
            return false;
        }

        string? phaseId = null;
        if (root.TryGetProperty("phaseId", out var phase))
        {
            if (phase.ValueKind == JsonValueKind.String)
            {
                phaseId = phase.GetString();
                if (phaseId is null || !MaintenancePhases.All.Contains(phaseId)) return false;
            }
            else if (phase.ValueKind != JsonValueKind.Null)
            {
                return false;
            }
        }

        string? targetId = null;
        if (root.TryGetProperty("targetId", out var target))
        {
            if (target.ValueKind == JsonValueKind.String)
            {
                targetId = target.GetString();
                if (string.IsNullOrWhiteSpace(targetId)) return false;
            }
            else if (target.ValueKind != JsonValueKind.Null)
            {
                return false;
            }
        }

        value = new MaintenanceEvent(
            schemaVersion,
            runId,
            sequence,
            timestamp.ToUniversalTime(),
            eventType,
            status,
            phaseId,
            targetId,
            messageDe,
            messageEn,
            details.Clone());
        return true;
    }

    private static bool TryGetText(JsonElement root, string name, out string value)
    {
        value = string.Empty;
        return root.TryGetProperty(name, out var property) &&
               property.ValueKind == JsonValueKind.String &&
               !string.IsNullOrWhiteSpace(value = property.GetString() ?? string.Empty);
    }

    private static bool TryGetGuid(JsonElement root, string name, out Guid value)
    {
        value = Guid.Empty;
        return TryGetText(root, name, out var text) && Guid.TryParse(text, out value);
    }

    private static bool TryGetInt32(JsonElement root, string name, out int value)
    {
        value = default;
        return root.TryGetProperty(name, out var property) &&
               property.ValueKind == JsonValueKind.Number &&
               property.TryGetInt32(out value);
    }

    private static bool TryGetInt64(JsonElement root, string name, out long value)
    {
        value = default;
        return root.TryGetProperty(name, out var property) &&
               property.ValueKind == JsonValueKind.Number &&
               property.TryGetInt64(out value);
    }

    private MaintenanceEvent? DegradeAndReturn(EventDegradationReason reason)
    {
        Degrade(reason);
        return null;
    }

    private void Degrade(EventDegradationReason reason)
    {
        _presentationMode = EventPresentationMode.Degraded;
        if (_degradationReason == EventDegradationReason.None)
        {
            _degradationReason = reason;
        }
    }
}
