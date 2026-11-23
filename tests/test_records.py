import unittest
from pathlib import Path

from src.records import load_records


class RecordInputTests(unittest.TestCase):
    def test_synthetic_observations_are_readable(self):
        root = Path(__file__).resolve().parents[1]
        data = load_records(root / "data" / "observations.json")
        self.assertEqual(data["format_version"], 1)
        self.assertGreater(len(data["scenarios"]), 0)


if __name__ == "__main__":
    unittest.main()
