"""
Reproducible Scientific Computation Platform — Clean-Room Domain Core
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import hashlib


@dataclass
class DomainRecord:
    record_id: str
    tenant_id: str
    payload: Dict[str, object]
    version: int = 1
    status: str = "ACTIVE"

    def digest(self) -> str:
        raw = f"{self.tenant_id}:{self.record_id}:{self.version}:{self.status}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class DomainEngine:
    """Enforces tenant isolation, idempotency, and invariant checks for Reproducible Scientific Computation Platform."""

    def __init__(self) -> None:
        self._store: Dict[str, DomainRecord] = {}
        self._idempotency: Dict[str, str] = {}

    def execute(self, tenant_id: str, record_id: str, idempotency_key: str, payload: Dict[str, object]) -> DomainRecord:
        if not tenant_id or not record_id or not idempotency_key:
            raise ValueError("tenant_id, record_id, and idempotency_key are required")
        scoped_idem = f"{tenant_id}:{idempotency_key}"
        if scoped_idem in self._idempotency:
            existing_key = self._idempotency[scoped_idem]
            return self._store[existing_key]

        scoped_key = f"{tenant_id}:{record_id}"
        existing = self._store.get(scoped_key)
        version = (existing.version + 1) if existing else 1
        rec = DomainRecord(record_id=record_id, tenant_id=tenant_id, payload=dict(payload), version=version)
        self._store[scoped_key] = rec
        self._idempotency[scoped_idem] = scoped_key
        return rec

    def get(self, tenant_id: str, record_id: str) -> Optional[DomainRecord]:
        return self._store.get(f"{tenant_id}:{record_id}")
