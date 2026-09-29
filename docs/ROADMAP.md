# Roadmap

## Phase 0 — Bootstrap

- [x] Create repository
- [x] Establish repository structure
- [x] Add Git safety rules for weights and secrets
- [x] Document initial architecture
- [x] Choose multi-model strategy
- [x] Choose Qwen3-8B as first AI baseline
- [x] Choose llama.cpp as first inference runtime
- [x] Choose full Kubernetes as orchestration platform
- [x] Define hybrid local + Oracle Cloud architecture
- [ ] Inventory all Kubernetes nodes
- [ ] Inventory local disks and usable storage
- [ ] Record network topology and link speeds

## Phase 1 — Kubernetes foundation

- [ ] Prepare Dell Precision T5810 primary control-plane/AI host
- [ ] Prepare ProLiant Oracle/storage gateway and warm-standby host
- [ ] Install full Kubernetes control plane
- [ ] Join Linux worker nodes
- [ ] Configure container runtime
- [ ] Configure cluster networking
- [ ] Configure namespaces, quotas, priorities, and node labels
- [ ] Reserve resources for business/AI workloads
- [ ] Place mining/background compute at lowest priority

## Phase 2 — Storage platform

- [ ] Inventory 500 GB+ local disks on each Linux worker and retained storage nodes
- [ ] Select Kubernetes persistent-storage layer
- [ ] Configure local/offline persistent volumes
- [ ] Define replication and failure policy
- [ ] Integrate OCI object/archive storage
- [ ] Configure local-to-cloud backup policy
- [ ] Test offline operation
- [ ] Test restore from OCI

## Phase 3 — Hardware and model benchmarking

- [ ] Inventory CPU, RAM, GPU/VRAM, disk, and OS by node
- [ ] Define realistic target model sizes
- [ ] Benchmark Qwen3-8B
- [ ] Benchmark alternate models
- [ ] Select quantization by node class
- [ ] Measure tokens/sec, memory, power, and network overhead

## Phase 4 — I2PS AI services

- [ ] Package llama.cpp inference service as OCI container image
- [ ] Deploy model service through Kubernetes
- [ ] Add prompt/system configuration
- [ ] Add local knowledge retrieval
- [ ] Add vector/index storage
- [ ] Add conversation/session layer
- [ ] Add evaluation harness
- [ ] Add model routing

## Phase 5 — Adaptation

- [ ] Curate training and evaluation data
- [ ] Run LoRA/QLoRA experiments if hardware permits
- [ ] Evaluate against baseline
- [ ] Document results and regressions

## Phase 6 — Hybrid operations

- [ ] Add monitoring
- [ ] Add authentication and access control
- [ ] Configure OCI connectivity, with ProLiant acting as dedicated storage/cloud gateway if retained
- [ ] Add backup and disaster-recovery workflows
- [ ] Back up Kubernetes state/configuration to ProLiant and OCI
- [ ] Test Dell failure and ProLiant recovery procedure
- [ ] Test node failure and workload relocation
- [ ] Add third control-plane member when automatic HA is required
- [ ] Test cloud-assisted recovery
