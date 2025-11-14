[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
# Aware-AI-Framework

**Author:** randolphpelican  
**License:** MIT

## Overview
The **Aware-AI-Framework** is an experimental platform for prototyping synthetic-consciousness architectures and nested-mind physics. It provides modular stages for federated sensory processing, energy-aware computation, codebook consolidation, and recursive closure to experiment with proto-awareness behaviours.

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
stage3_recursive_closure/     # recursive self-reference and system unification
stage4_experimental_interface/# I/O and adaptive runtime experiments
ai_core/                      # shared base classes, energy manager, and message bus
utils/                        # logging, math helpers, config tools
experiments/                  # prebuilt test configurations and simulations
tests/                        # validation scripts and regression tests
docs/                         # documentation, diagrams, and papers
```

## Installation
```bash
git clone https://github.com/randolphpelican/Aware-AI-Framework.git
cd Aware-AI-Framework
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running a Basic Experiment
```bash
python experiments/basic_awareness_test.py
```

## Contributing
Pull requests are welcome! Focus on clarity, modularity, and reproducibility. Include documentation for new modules and seed data for reproducible runs.

## License
MIT © randolphpelican
## Experiments

To run prebuilt experiments:

```bash
# Activate your virtual environment first
source venv/bin/activate

# Run the basic demo
python -m experiments.basic_awareness_test

# Run the template experiment
python -m experiments.experiment_template
```

### Adding New Experiments

1. Create a new `.py` file in `experiments/`.
2. Import stage classes (`BaseDemodulator`, `CodebookManager`, `ClosureController`) and `log` from `utils.helpers`.
3. Follow the `experiment_template.py` structure.
4. Add logging for all major steps.
5. Ensure reproducibility with seed data if needed.
## Documentation

Diagrams, detailed explanations, and papers are stored in the `docs/` folder.  
Add markdown or PDF files as needed. Example:

```
docs/architecture_overview.pdf
docs/stage_flow_diagram.md
```
