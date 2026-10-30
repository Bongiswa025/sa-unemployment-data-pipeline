
import sqlite3
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "unemployment.db"


class TestDatabase(unittest.TestCase):

    def test_database_exists(self):
        self.assertTrue(DATABASE_FILE.exists())

    def test_unemployment_table_exists(self):
        with sqlite3.connect(DATABASE_FILE) as connection:
            result = connection.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name='unemployment'"
            )
            self.assertIsNotNone(result.fetchone())

    def test_database_has_records(self):
        with sqlite3.connect(DATABASE_FILE) as connection:
            result = connection.execute(
                "SELECT COUNT(*) FROM unemployment"
            )
            total = result.fetchone()[0]
            self.assertGreater(total, 0)

    def test_required_columns(self):
        required = {
            "id",
            "province",
            "age",
            "gender",
            "qualification",
            "employment_status",
            "age_group",
        }

        with sqlite3.connect(DATABASE_FILE) as connection:
            result = connection.execute(
                "PRAGMA table_info(unemployment)"
            )
            actual = {row[1] for row in result.fetchall()}

        self.assertTrue(required.issubset(actual))


if __name__ == "__main__":
    unittest.main()
