package core

import "testing"

func TestEngineIdempotencyAndIsolation(t *testing.T) {
	eng := NewEngine()
	r1, err := eng.Apply("tenant-1", "res-1", "req-1", "alpha")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	r2, err := eng.Apply("tenant-1", "res-1", "req-1", "beta")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if r1.Digest != r2.Digest || r2.Version != 1 {
		t.Fatalf("expected idempotent replay")
	}
	if _, ok := eng.Get("tenant-2", "res-1"); ok {
		t.Fatalf("cross-tenant leak detected")
	}
}
