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


## ADR-0002 — Multi-model architecture with Qwen3-8B baseline

**Status:** Accepted  
**Date:** 2026-09-28

### Decision

I2PS AI will support multiple interchangeable open-weight models behind a common runtime interface.

The first baseline model family is **Qwen3-8B**. The canonical first runtime is **llama.cpp** using GGUF models.

The exact quantization and context allocation will be selected after measuring the ProLiant's available RAM, CPU instruction support, storage, and any available GPU/accelerator.

### Why Qwen3-8B first

- permissive Apache 2.0 release
- practical 8B-class size for local experimentation
- strong general, coding, STEM, multilingual, and reasoning capabilities
- supports reasoning and fast-response modes
- broad local-runtime support

### Runtime policy

**llama.cpp** is the canonical baseline runtime because it supports CPU-first inference, quantized GGUF models, CPU/GPU hybrid inference, and an OpenAI-compatible local server.

Ollama may be added as a convenience/model-management layer.

vLLM may be added later for high-throughput GPU serving if suitable accelerator hardware is introduced.

### Multi-model policy

Models are not permanently hard-coded into the application. The system will use a model registry and may switch models by task or benchmark result.

Initial comparison candidates:

1. Qwen3-8B — primary baseline
2. Qwen3-14B — larger Qwen candidate if memory permits
3. Mistral 3 8B — permissive alternative baseline
4. Gemma 3 4B / 12B — compact multimodal alternatives
5. Larger MoE or multimodal models — deferred until hardware supports them

Normally only the selected model(s) required for a workload should be resident in memory. Keeping several model files on disk is acceptable; loading all of them simultaneously is not a requirement.

### Consequence

I2PS AI becomes model-portable. We can benchmark, replace, specialize, or route between models without redesigning the application.
