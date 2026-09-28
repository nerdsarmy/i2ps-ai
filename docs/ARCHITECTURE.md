# I2PS AI — Initial Architecture

## Principle

The project does not assume a specific foundation model at bootstrap. The first model will be selected after hardware measurement, license review, and benchmarking.

## Layers

### 1. Foundation model

An open-weight model selected after benchmarking and license review.

### 2. Runtime

A local inference engine selected according to CPU/GPU hardware, memory limits, operating system, and model format.

### 3. Knowledge layer

I2PS-specific documents and structured knowledge should initially be added through retrieval rather than baked into model weights. This keeps knowledge auditable and updateable.

### 4. Evaluation

A repeatable evaluation suite will measure at minimum:

- correctness
- instruction following
- hallucination rate
- domain knowledge
- latency
- memory consumption
- tokens per second

### 5. Adaptation

Fine-tuning, LoRA/QLoRA, preference optimization, or other alignment techniques will be introduced only when evaluation demonstrates a specific limitation that adaptation can address.

## External research

Public Anthropic research, alignment datasets, and Constitutional AI material may be studied as references. They are not Claude model weights and must not be treated as a downloadable Claude model.

## Repository policy

Model weights, large datasets, private documents, generated checkpoints, secrets, tokens, and credentials must never be committed directly to Git.
