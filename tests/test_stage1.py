import unittest
from stage1_demodulators.base import BaseDemodulator

class TestStage1(unittest.TestCase):
    def test_process_frame(self):
        demod = BaseDemodulator()
        output = demod.process_frame("test_frame")
        self.assertIsInstance(output, dict)
        self.assertIn("stage1_output", output)
        self.assertEqual(output["stage1_output"], "test_frame")

if __name__ == "__main__":
    unittest.main()
