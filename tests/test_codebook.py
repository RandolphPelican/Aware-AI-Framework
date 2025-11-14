import unittest
from stage1_demodulators.base import BaseDemodulator
from stage2_codebook.codebook_manager import CodebookManager
from stage3_recursive_closure.closure_controller import ClosureController

class TestStage1(unittest.TestCase):
    def test_process_frame(self):
        demod = BaseDemodulator()
        output = demod.process_frame("test_frame")
        self.assertIsInstance(output, dict)
        self.assertIn("stage1_output", output)
        self.assertEqual(output["stage1_output"], "test_frame")

class TestStage2(unittest.TestCase):
    def test_merge(self):
        cbm = CodebookManager()
        data = [{"dummy": 1}]
        output = cbm.merge(data)
        self.assertIsInstance(output, dict)
        self.assertIn("stage2_merged", output)
        self.assertEqual(output["stage2_merged"], len(data))
        self.assertIn("data", output)
        self.assertEqual(output["data"], data)

class TestStage3(unittest.TestCase):
    def test_iterate(self):
        closure = ClosureController()
        data = {"test": "value"}
        output = closure.iterate(data, iterations=3)
        self.assertIsInstance(output, dict)
        self.assertIn("stage3_iterations", output)
        self.assertEqual(output["stage3_iterations"], 3)
        self.assertIn("final_data", output)
        self.assertEqual(output["final_data"], data)

if __name__ == "__main__":
    unittest.main()
