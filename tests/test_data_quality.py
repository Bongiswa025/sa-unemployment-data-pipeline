
import unittest
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "cleaned_unemployment.csv"


class TestDataQuality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv(DATA_FILE)

    def test_required_columns(self):
        required = [
            "id", "province", "age", "gender",
            "qualification", "employment_status", "age_group"
        ]
        for column in required:
            self.assertIn(column, self.data.columns)

    def test_no_duplicate_ids(self):
        self.assertFalse(self.data["id"].duplicated().any())

    def test_no_missing_values(self):
        columns = [
            "province", "age", "gender",
            "qualification", "employment_status"
        ]
        self.assertFalse(self.data[columns].isnull().any().any())

    def test_valid_ages(self):
        ages = pd.to_numeric(self.data["age"], errors="coerce")
        self.assertTrue(ages.notna().all())
        self.assertTrue(ages.between(15, 100).all())

    def test_age_groups_exist(self):
        self.assertTrue(self.data["age_group"].notna().all())


if __name__ == "__main__":
    unittest.main()
