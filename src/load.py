
import sqlite3
from pathlib import Path

import pandas as pd

# Locate our main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Cleaned CSV file
DATA_FILE = BASE_DIR / "data" / "processed" / "cleaned_unemployment.csv"

# SQLite database location
DATABASE_FILE = BASE_DIR / "data" / "unemployment.db"


def load_data():
    """Load cleaned unemployment records into SQLite."""

    if not DATA_FILE.exists():
        print("Cleaned dataset not found.")
        print("Please run python src/transform.py first.")
        return

    # Read cleaned unemployment records
    data = pd.read_csv(DATA_FILE)

    # Connect to SQLite (creates database if missing)
    with sqlite3.connect(DATABASE_FILE) as connection:

        # Store records in a database table
        data.to_sql(
            "unemployment",
            connection,
            if_exists="replace",
            index=False
        )

        # Verify how many records were stored
        cursor = connection.execute(
            "SELECT COUNT(*) FROM unemployment"
        )
        total = cursor.fetchone()[0]

    print("Database created successfully!")
    print("Unemployment records stored:", total)
    print("Database location:", DATABASE_FILE)


if __name__ == "__main__":
    load_data()
