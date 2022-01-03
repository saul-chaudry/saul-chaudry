# Architectural Decisions — Change Data Capture & Search Projection Platform

## 1. Explicit Invariant Enforcement at the Domain Boundary
Core invariants—including tenant isolation, idempotent command handling, and deterministic state transitions—are enforced directly in the domain engine with zero external framework coupling.

## 2. Deterministic Verification (`java Main.java`)
All state mutations and security boundaries are covered by self-contained executable tests so reviewers can verify correctness in seconds without provisioning external cloud infrastructure.
