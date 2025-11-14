import unittest
from stage3_recursive_closure.closure_controller import ClosureController

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
