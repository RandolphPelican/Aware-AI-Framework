"""
basic_awareness_test.py

A tiny feed through stage1 → stage2 → stage3 to verify the framework runs.
"""

from stage1_demodulators.base import BaseDemodulator
from stage2_codebook.codebook_manager import CodebookManager
from stage3_recursive import ClosureController  # <- corrected import

def run_demo():
    print("Starting Basic Awareness Demo...")

    # Stage 1: Dummy demodulator
    demodulator = BaseDemodulator()
    stage1_output = demodulator.process_frame("synthetic_frame")
    print("Stage 1 output:", stage1_output)

    # Stage 2: Codebook consolidation
    codebook = CodebookManager()
    consolidated = codebook.merge([stage1_output])
    print("Stage 2 output:", consolidated)

    # Stage 3: Recursive closure
    closure = ClosureController(codebook)
    awareness = closure.iterate(consolidated, iterations=2)
    print("Stage 3 output:", awareness)

if __name__ == "__main__":
    run_demo()
