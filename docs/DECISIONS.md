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


## ADR-0003 — Full Kubernetes and hybrid on-prem/OCI platform

**Status:** Accepted  
**Date:** 2026-09-28

### Decision

Use full upstream Kubernetes rather than K3s for the I2PS platform.

The HP ProLiant is the primary on-prem server/control-plane host. Existing Linux machines join as Kubernetes worker nodes and contribute compute and storage.

Docker-compatible OCI images are the standard packaging format. Kubernetes is the orchestration layer.

Oracle Cloud Infrastructure extends the local cluster with cloud storage, backup, networking, recovery, and cloud-executed workloads.

### Storage strategy

Use two coordinated storage tiers:

1. **Local/offline tier** built from the disks already installed across the Linux cluster.
2. **OCI cloud tier** for off-site backup, object storage, archive, recovery, and selected cloud workloads.

The system must continue supporting useful local operation without dependence on OCI connectivity.

### Resource priority

Kubernetes resource policy must prioritize business services and I2PS AI above background compute. Mining remains a subordinate workload that uses spare capacity only.

### Consequence

I2PS AI is no longer designed as a single-server application. It is a Kubernetes-managed service within a distributed hybrid platform spanning the local Linux cluster and Oracle Cloud.


## ADR-0004 — T5810 becomes primary Kubernetes/AI host; ProLiant reduced to storage/cloud role

**Status:** Accepted  
**Date:** 2026-09-29

### Decision

If the Dell Precision T5810 is acquired, it becomes the primary Kubernetes control-plane host and primary AI worker.

The HP ProLiant is removed from Kubernetes control-plane and AI duties. If retained, it is dedicated to cloud/storage functions only, including remote file access, local storage services, backup/synchronization, and Oracle Cloud integration.

### Reason

The T5810 is the more suitable host for compute-intensive AI and orchestration workloads. Keeping the ProLiant focused on storage/cloud duties isolates those services from AI load and simplifies its operational role.

### Consequence

The platform roles become:

- Mac controller: administration
- Dell Precision T5810: Kubernetes control plane + primary AI worker
- Linux worker fleet: additional Kubernetes compute/storage workers
- HP ProLiant: dedicated storage/cloud gateway if retained
- Oracle Cloud Infrastructure: off-site/cloud extension

The ProLiant is no longer a required part of the AI compute path.


## ADR-0005 — ProLiant as Dell failover host and Oracle Cloud gateway

**Status:** Accepted  
**Date:** 2026-09-29

### Decision

The Dell Precision T5810 remains the primary Kubernetes control-plane host and primary AI worker.

The HP ProLiant has a dual infrastructure role:

1. Oracle Cloud / remote-storage gateway during normal operation.
2. Warm standby and recovery host for the Dell T5810.

The ProLiant maintains synchronized cluster configuration, backups, recovery material, and the services required to restore or temporarily assume orchestration if the Dell fails.

### Availability model

The Dell/ProLiant pair is treated as primary/standby redundancy, not as a two-member automatic Kubernetes quorum.

For true automatic control-plane high availability, the target topology is three control-plane members or another quorum-safe datastore design.

### Failure behavior

If the Dell is unavailable:

- the ProLiant assumes fallback orchestration duties;
- essential platform/storage/cloud services remain available where possible;
- Linux workers remain usable;
- AI workloads may be rescheduled to capable workers;
- AI performance may be reduced because the ProLiant has substantially less memory/compute capacity than the primary AI host.

### Consequence

The ProLiant is retained as useful infrastructure even when the T5810 is present: it provides Oracle integration, remote storage, backup/recovery, and a recovery path for failure of the primary server.
