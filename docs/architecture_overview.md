# Aware-AI-Framework Architecture Overview

This document describes the high-level architecture of the Aware-AI-Framework.

## Stages

1. **Stage 1: Federated Demodulators**
   - Handles sensory inputs: audio, vision, temporal.
   - Outputs standardized data frames for further processing.

2. **Stage 2: Codebook Consolidation**
   - Merges stage1 outputs into higher-order codebooks.
   - Prepares data for recursive closure.

3. **Stage 3: Recursive Closure**
   - Self-referential loops to simulate proto-awareness.
   - Iteratively refines internal state.

4. **Stage 4: Experimental Interface**
   - Handles I/O, adaptive runtime experiments.
   - Optional hooks for quantum or external interfaces.

5. **Core Utilities**
   - `ai_core/` contains shared base classes, energy manager, message bus.
   - `utils/` contains logging, helper functions, and configuration tools.

## Experiment Workflow

- Create new experiments in `experiments/` using `experiment_template.py`.
- Use logging from `utils.helpers` to monitor data flow.
- Use the virtual environment to ensure dependency consistency.
