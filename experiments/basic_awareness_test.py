"""
basic_awareness_test.py

A tiny feed through stage1 → stage2 → stage3 to verify the framework runs.
"""

from stage1_demodulators.base import BaseDemodulator
from stage2_codebook.codebook_manager import CodebookManager
from stage3_recursive_closure.closure_controller import ClosureController

def run_demo():
    print("Starting Basic Awareness Demo...")

    # Stage 1: Dummy demodulator
    demodulator = BaseDemodulator()
    sensory_data = demodulator.process_frame("synthetic_frame")
    print("Stage 1 output:", sensory_data)

    # Stage 2: Codebook consolidation
    codebook = CodebookManager()
    consolidated = codebook.merge([sensory_data])
    print("Stage 2 output:", consolidated)

    # Stage 3: Recursive closure
    closure = ClosureController()
    awareness = closure.iterate(consolidated, iterations=2)
    print("Stage 3 output:", awareness)

    print("Demo completed successfully.")

if __name__ == "__main__":
    run_demo()
