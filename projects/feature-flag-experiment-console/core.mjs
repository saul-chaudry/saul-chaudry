import crypto from "node:crypto";

export class DomainEngine {
  constructor() {
    this.store = new Map();
    this.idempotency = new Map();
  }

  execute(tenantId, entityId, idemKey, payload) {
    if (!tenantId || !entityId || !idemKey) {
      throw new Error("Missing tenantId, entityId, or idemKey");
    }
    const scopedIdem = `${tenantId}:${idemKey}`;
    if (this.idempotency.has(scopedIdem)) {
      return this.store.get(this.idempotency.get(scopedIdem));
    }
    const scopedKey = `${tenantId}:${entityId}`;
    const prev = this.store.get(scopedKey);
    const version = prev ? prev.version + 1 : 1;
    const digest = crypto
      .createHash("sha256")
      .update(`${scopedKey}:${version}:${JSON.stringify(payload)}`)
      .digest("hex");
    const rec = { tenantId, entityId, version, payload, digest };
    this.store.set(scopedKey, rec);
    this.idempotency.set(scopedIdem, scopedKey);
    return rec;
  }

  get(tenantId, entityId) {
    return this.store.get(`${tenantId}:${entityId}`) ?? null;
  }
}
