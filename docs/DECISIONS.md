# Engineering Decisions

This file records decisions that materially affect the I2PS AI architecture.

## ADR-0001 — Start model-neutral

**Status:** Accepted  
**Date:** 2026-09-28

### Decision

Do not select a foundation model before measuring available hardware and benchmarking realistic candidates.

### Reason

Model size, quantization, runtime, latency, memory use, licensing, and training options are tightly coupled to the hardware actually available. Selecting a model first would create unnecessary constraints.

### Consequence

The initial repository contains interfaces, configuration, diagnostics, and documentation, but no hard-coded model dependency.
