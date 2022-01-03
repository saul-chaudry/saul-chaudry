using System.Security.Cryptography;
using System.Text;

var engine = new DomainEngine();
var r1 = engine.Apply("tenant-a", "entity-1", "idem-1", "ACTIVE");
var r2 = engine.Apply("tenant-a", "entity-1", "idem-1", "MUTATED");

if (r1.Digest != r2.Digest || r2.Version != 1)
    throw new InvalidOperationException("Idempotency invariant failed.");

if (engine.Get("tenant-b", "entity-1") is not null)
    throw new InvalidOperationException("Tenant isolation invariant failed.");

Console.WriteLine("Verified Manufacturing Quality & Traceability Platform: OK");

public sealed record DomainEntry(string TenantId, string EntityId, int Version, string State, string Digest);

public sealed class DomainEngine
{
    private readonly Dictionary<string, DomainEntry> _store = new();
    private readonly Dictionary<string, string> _idempotency = new();

    public DomainEntry Apply(string tenantId, string entityId, string idemKey, string state)
    {
        if (string.IsNullOrWhiteSpace(tenantId) || string.IsNullOrWhiteSpace(entityId) || string.IsNullOrWhiteSpace(idemKey))
            throw new ArgumentException("Invalid domain context.");

        var scopedIdem = $"{tenantId}:{idemKey}";
        if (_idempotency.TryGetValue(scopedIdem, out var existingKey))
            return _store[existingKey];

        var scopedKey = $"{tenantId}:{entityId}";
        var nextVer = _store.TryGetValue(scopedKey, out var prev) ? prev.Version + 1 : 1;
        var hash = Convert.ToHexString(SHA256.HashData(Encoding.UTF8.GetBytes($"{scopedKey}:{nextVer}:{state}")));
        var entry = new DomainEntry(tenantId, entityId, nextVer, state, hash);
        _store[scopedKey] = entry;
        _idempotency[scopedIdem] = scopedKey;
        return entry;
    }

    public DomainEntry? Get(string tenantId, string entityId) =>
        _store.TryGetValue($"{tenantId}:{entityId}", out var e) ? e : null;
}
