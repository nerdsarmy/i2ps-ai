# I2PS AI

I2PS AI is an independent engineering project for building, evaluating, and operating a locally controlled AI system using open-weight foundation models and reproducible workflows.

## Current status

**Phase 0 — Bootstrap**

The repository is intentionally model-neutral at the start. We will select the first foundation model only after measuring the available hardware, checking licenses, and benchmarking realistic candidates.

## Goals

- Use an open-weight foundation model rather than depend on a proprietary hosted model.
- Keep model choice modular so the foundation model can be replaced without redesigning the project.
- Separate inference, knowledge retrieval, evaluation, adaptation, and serving layers.
- Keep model weights, large datasets, secrets, private documents, and generated checkpoints out of Git.
- Record major architecture and model decisions.
- Start locally, measure first, and scale hardware only when evidence requires it.

## Repository structure

```text
i2ps-ai/
├── configs/       Model and runtime configuration
├── docs/          Architecture, decisions, and roadmap
├── scripts/       Setup, diagnostics, downloads, and benchmarks
├── src/i2ps_ai/   Python package
├── training/      Fine-tuning and alignment workflows
└── tests/         Automated tests
```

## Development plan

1. Inventory available compute.
2. Shortlist current open-weight models.
3. Review licenses and deployment constraints.
4. Benchmark baseline inference.
5. Select the first foundation model.
6. Add a local knowledge/RAG layer.
7. Build an evaluation harness.
8. Fine-tune or align only when evaluation shows a concrete need.

## Important

This repository does **not** contain Claude model weights or any other proprietary model weights. Public Anthropic research, alignment datasets, and Constitutional AI material may be studied as references, but the I2PS model will use an independently selected open-weight foundation model.

## Project owner

I2PS Engineering
