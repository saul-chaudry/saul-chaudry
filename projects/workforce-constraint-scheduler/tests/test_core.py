import unittest
from core import DomainEngine


class DomainEngineTests(unittest.TestCase):
    def test_idempotent_execution_and_tenant_isolation(self) -> None:
        engine = DomainEngine()
        r1 = engine.execute("tenant-a", "item-1", "idem-100", {"metric": 42})
        r2 = engine.execute("tenant-a", "item-1", "idem-100", {"metric": 99})
        self.assertEqual(r1.version, 1)
        self.assertEqual(r1.digest(), r2.digest())
        self.assertIsNone(engine.get("tenant-b", "item-1"))

    def test_version_increment_on_distinct_operation(self) -> None:
        engine = DomainEngine()
        engine.execute("tenant-a", "item-1", "idem-1", {"step": "init"})
        updated = engine.execute("tenant-a", "item-1", "idem-2", {"step": "verified"})
        self.assertEqual(updated.version, 2)


if __name__ == "__main__":
    unittest.main()
