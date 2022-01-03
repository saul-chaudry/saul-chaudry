import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.HexFormat;
import java.util.Map;

public class Main {
    record DomainState(String tenantId, String resourceId, int version, String payload, String digest) {}

    static final class Engine {
        private final Map<String, DomainState> store = new HashMap<>();
        private final Map<String, String> idempotency = new HashMap<>();

        public synchronized DomainState apply(String tenantId, String resourceId, String idemKey, String payload) throws Exception {
            if (tenantId == null || tenantId.isBlank() || resourceId == null || resourceId.isBlank() || idemKey == null || idemKey.isBlank()) {
                throw new IllegalArgumentException("Missing required context");
            }
            String scopedIdem = tenantId + ":" + idemKey;
            if (idempotency.containsKey(scopedIdem)) {
                return store.get(idempotency.get(scopedIdem));
            }
            String scopedKey = tenantId + ":" + resourceId;
            int nextVersion = store.containsKey(scopedKey) ? store.get(scopedKey).version() + 1 : 1;
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            String digest = HexFormat.of().formatHex(md.digest((scopedKey + ":" + nextVersion + ":" + payload).getBytes(StandardCharsets.UTF_8)));
            DomainState state = new DomainState(tenantId, resourceId, nextVersion, payload, digest);
            store.put(scopedKey, state);
            idempotency.put(scopedIdem, scopedKey);
            return state;
        }

        public synchronized DomainState get(String tenantId, String resourceId) {
            return store.get(tenantId + ":" + resourceId);
        }
    }

    public static void main(String[] args) throws Exception {
        Engine engine = new Engine();
        DomainState s1 = engine.apply("tenant-alpha", "order-101", "idem-1", "RESERVED");
        DomainState s2 = engine.apply("tenant-alpha", "order-101", "idem-1", "DUPLICATE");
        if (!s1.digest().equals(s2.digest()) || s2.version() != 1) {
            throw new AssertionError("Idempotency invariant violated");
        }
        if (engine.get("tenant-beta", "order-101") != null) {
            throw new AssertionError("Tenant isolation invariant violated");
        }
        System.out.println("Verified Product Catalog & Schema Governance Platform: OK");
    }
}
