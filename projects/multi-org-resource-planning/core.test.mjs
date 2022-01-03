import test from "node:test";
import assert from "node:assert/strict";
import { DomainEngine } from "./core.mjs";

test("enforces idempotency and tenant isolation", () => {
  const engine = new DomainEngine();
  const r1 = engine.execute("tenant-a", "doc-1", "k-1", { approved: true });
  const r2 = engine.execute("tenant-a", "doc-1", "k-1", { approved: false });
  assert.equal(r1.digest, r2.digest);
  assert.equal(r2.version, 1);
  assert.equal(engine.get("tenant-b", "doc-1"), null);
});
