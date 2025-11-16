# experiments/example_experiment.py
from stage1_demodulators.base import BaseDemodulator
from stage2_codebook.codebook_manager import CodebookManager
from stage3_recursive_closure.closure_controller import ClosureController

def run_example():
    print("Starting Example Experiment...")

    # Stage 1: Initialize a dummy demodulator
    demod = BaseDemodulator()
    demod.update("example_input")
    print("Stage 1 output:", demod.get_state())

    # Stage 2: Create a codebook and add stage 1 data
    codebook = CodebookManager()
    codebook.add("stage1", demod.get_state())
    print("Stage 2 output:", codebook.get("stage1"))

    # Stage 3: Recursive closure example
    closure = ClosureController(codebook)
    closure_result = closure.run_iterations(2)
    print("Stage 3 output:", closure_result)

    print("Example Experiment Completed Successfully.")

if __name__ == "__main__":
    run_example()
