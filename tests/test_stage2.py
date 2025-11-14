import unittest
from stage2_codebook.codebook_manager import CodebookManager

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

if __name__ == "__main__":
    unittest.main()
