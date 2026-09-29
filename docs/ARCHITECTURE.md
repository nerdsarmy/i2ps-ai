# I2PS AI — Platform Architecture

## Core platform

I2PS AI runs as part of the wider I2PS distributed platform.

- **Full Kubernetes** provides orchestration, scheduling, health management, service discovery, policy, and workload placement.
- **Docker-compatible OCI images** are the packaging format for workloads.
- **Dell Precision T5810** is the primary on-prem Kubernetes control-plane host and primary AI worker.
- **Linux worker nodes** provide additional compute and local storage.
- **HP ProLiant / Worker 11**, if retained, is dedicated to cloud/storage duties only: remote file access, storage services, backup/synchronization, and Oracle Cloud integration. It is not the Kubernetes control plane and is not an AI inference node.
- **Oracle Cloud Infrastructure (OCI)** extends the platform into the cloud for storage, backup, networking, recovery, and cloud-executed workloads.
- **Mac controller** remains the administrative workstation used to manage the platform over SSH and Kubernetes tooling.
- The ProLiant may remain outside the Kubernetes compute path entirely so storage/cloud duties stay isolated from AI and orchestration load.

## Workload priority

1. Business-critical services
2. I2PS AI and internal platform services
3. Storage, backup, monitoring, and maintenance services
4. Background compute such as mining

Background workloads must yield CPU, RAM, storage I/O, and network capacity whenever higher-priority services need them.

## AI architecture

### Model layer

I2PS AI supports multiple interchangeable open-weight models.

Primary baseline:
- Qwen3-8B

Additional candidates:
- Qwen3-14B
- Mistral 3 8B
- Gemma 3 4B
- Gemma 3 12B

Models are selected and routed by workload rather than permanently hard-coded into the application.

### Runtime layer

The initial inference runtime is **llama.cpp** using GGUF models.

Other runtimes may be introduced where useful:
- Ollama for simplified model management
- vLLM for future accelerator-backed high-throughput serving

### Scheduling model

Kubernetes schedules AI services onto suitable nodes according to CPU, RAM, accelerator availability, storage locality, health, and workload priority.

Most inference workloads should run as independent model services or replicas. Experimental cross-node model splitting may be tested separately where justified by hardware and network performance.

## Hybrid storage architecture

The Linux cluster contains substantial local disk capacity. Each node's local disks remain individually addressable but are incorporated into a managed storage layer.

### Local / offline tier

Purpose:
- model files
- local datasets
- vector indexes
- application state
- caches
- snapshots
- private documents
- offline operation when Internet/cloud access is unavailable

The storage layer must preserve node-local awareness while presenting persistent storage to Kubernetes workloads.

### Cloud tier — Oracle Cloud Infrastructure

OCI provides the off-site/cloud tier for:
- object storage
- backup copies
- archival storage
- disaster recovery
- workload recovery
- cloud execution when required
- secure connectivity between on-prem and cloud resources

Cloud storage is an extension of the local platform, not a replacement for local storage.

### Data policy

Data must be classified before cloud synchronization.

- public/non-sensitive data may be synchronized normally
- internal/private data requires controlled access and encryption
- secrets and credentials must not be stored in Git
- selected workloads must remain capable of operating entirely offline

## Knowledge layer

I2PS-specific information should initially be supplied through retrieval and structured data rather than permanently embedded into model weights.

This supports:
- auditable knowledge
- rapid updates
- local-only private knowledge
- separate cloud and offline data policies

## Resilience

The target platform supports:
- local execution without cloud dependency
- replicated services
- persistent storage
- node failure recovery
- backup to OCI
- workload relocation between eligible nodes
- later cloud failover for selected services

## External research

Public Anthropic research, alignment datasets, and Constitutional AI material may be studied as references. They are not Claude model weights and must not be treated as a downloadable Claude model.

## Repository policy

Model weights, large datasets, private documents, generated checkpoints, secrets, tokens, and credentials must never be committed directly to Git.
