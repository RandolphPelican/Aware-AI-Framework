# Aware-AI-Framework

**Author:** randolphpelican  
**License:** MIT

## Overview
The **Aware-AI-Framework** is an experimental research platform for prototyping synthetic-consciousness architectures and nested-mind physics. It provides modular stages for federated sensory processing, energy-aware computation, codebook consolidation, and recursive closure to experiment with proto-awareness behaviours.

> Warning: experimental research code. Not production-ready. Use for research, simulation, and educational purposes only.

## Key Features
- **Federated Demodulators** — independent modules for audio, vision, and temporal inputs.
- **Energy-Subsidy Manager** — dynamically allocates computation based on cost/benefit.
- **Codebook Consolidation** — merges local subsystem representations into higher-order codebooks.
- **Recursive Closure Architecture** — supports self-referential loops for proto-awareness experiments.
- **Modular Stages** — clearly separated stages to compose experiments and swap implementations.

## Repo layout
```
stage1_demodulators/          # demodulator implementations (audio, vision, temporal)
stage2_codebook/              # codebook management & consolidation
stage3_recursive_closure/     # recursive closure loops & controllers
stage4_experimental_interface/# AI ↔ quantum / simulator interface modules
ai_core/                      # core utilities, agents, scheduler
experiments/                  # example experiments / notebooks / scripts
utils/                        # helper functions
tests/                        # unit tests & CI hooks
docs/                         # architecture diagrams, API docs, design notes
```

## Quickstart (dev)
1. Clone:
```bash
git clone https://github.com/randolphpelican/Aware-AI-Framework.git
cd Aware-AI-Framework
```
2. Create Python virtualenv and install:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run a minimal demo (examples/demo_pipeline.py):
```bash
python experiments/demo_pipeline.py
```

## Example usage
- `experiments/demo_pipeline.py` runs a tiny feed of synthetic sensory frames through stage1 → stage2 → stage3 and prints diagnostic metrics.
- `stage1_demodulators/` contains pluggable class interfaces: `BaseDemodulator`, `AudioDemodulator`, `VisionDemodulator`, `TemporalDemodulator`.
- `stage2_codebook/` exposes `CodebookManager` with `merge`, `prune`, and `export` APIs.
- `stage3_recursive_closure/` exposes `ClosureController` with configurable iteration depth and energy budget.

## Development tips
- Keep stage boundaries thin — pass small, typed objects (dataclasses) between modules.
- Prefactor interfaces in `ai_core/interfaces.py` so experiments swap implementations without changing orchestration.
- Put heavy numeric code in `ai_core/compute/` and keep it vectorised (NumPy / JAX / PyTorch depending on need).

## Tests & CI
- Add unit tests to `tests/` and enable GitHub Actions: lint, unit tests, and optional mypy/type checks.
- Add small integration test that runs `demo_pipeline.py` with a tiny dataset.

## Contribution
See `CONTRIBUTING.md` for guidelines. Please open issues for design discussions before major PRs.

## License
MIT — see `LICENSE`.

## Contact
Open issues or PRs on GitHub; include reproducible experiments and seed data where possible.
