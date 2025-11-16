"""
neural_feedback_test.py

A minimal test of Stage 1 → Stage 2 → Stage 3 using synthetic neural feedback.
"""

from stage1_demodulators.base import BaseDemodulator
from stage2_codebook.codebook_manager import CodebookManager
from stage3_recursive import ClosureController  # <- corrected import

def run_demo():
    print("Starting Neural Feedback Demo...")

    # Stage 1: Dummy demodulator
    demodulator = BaseDemodulator()
    stage1_output = demodulator.process_frame({"signal": [0.1, 0.5, 0.3]})
    print("Stage 1 output:", stage1_output)

    # Stage 2: Codebook consolidation
    codebook = CodebookManager()
    consolidated = codebook.merge([stage1_output])
    print("Stage 2 output:", consolidated)

    # Stage 3: Recursive closure
    closure = ClosureController(codebook)
    awareness = closure.iterate(consolidated, iterations=3)
    print("Stage 3 output:", awareness)

if __name__ == "__main__":
    run_demo()
