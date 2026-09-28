# Roadmap

## Phase 0 — Bootstrap

- [x] Create repository
- [x] Establish repository structure
- [x] Add Git safety rules for weights and secrets
- [x] Document initial architecture
- [ ] Inventory target hardware
- [ ] Record first architecture decision

## Phase 1 — Hardware and model selection

- [ ] Inventory CPU, RAM, GPU/VRAM, disk, and OS
- [ ] Define realistic target model sizes
- [ ] Shortlist current open-weight models
- [ ] Review licenses
- [ ] Benchmark inference candidates
- [ ] Select first base model

## Phase 2 — Local assistant

- [ ] Implement inference adapter
- [ ] Add prompt/system configuration
- [ ] Add local knowledge retrieval
- [ ] Add conversation/session layer
- [ ] Add evaluation harness

## Phase 3 — Adaptation

- [ ] Curate training and evaluation data
- [ ] Run LoRA/QLoRA experiment if hardware permits
- [ ] Evaluate against baseline
- [ ] Document results and regressions

## Phase 4 — Serving

- [ ] Package model runtime
- [ ] Add API
- [ ] Add authentication
- [ ] Add monitoring
- [ ] Define deployment/update process
