
import sqlite3
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "unemployment.db"


def analyse_unemployment():
    if not DATABASE_FILE.exists():
        print("Database not found. Run python src/load.py first.")
        return

    with sqlite3.connect(DATABASE_FILE) as connection:

        # Count unemployed people by province
        province_query = """
            SELECT province, COUNT(*) AS total_unemployed
            FROM unemployment
            WHERE employment_status = 'Unemployed'
            GROUP BY province
            ORDER BY total_unemployed DESC
        """

        print("\nUNEMPLOYMENT BY PROVINCE")
        print(pd.read_sql_query(province_query, connection).to_string(index=False))

        # Count unemployed people by age group
        age_query = """
            SELECT age_group, COUNT(*) AS total_unemployed
            FROM unemployment
            WHERE employment_status = 'Unemployed'
            GROUP BY age_group
            ORDER BY age_group
        """

        print("\nUNEMPLOYMENT BY AGE GROUP")
        print(pd.read_sql_query(age_query, connection).to_string(index=False))

        # Count unemployed people by qualification
        qualification_query = """
            SELECT qualification, COUNT(*) AS total_unemployed
            FROM unemployment
            WHERE employment_status = 'Unemployed'
            GROUP BY qualification
            ORDER BY total_unemployed DESC
        """

        print("\nUNEMPLOYMENT BY QUALIFICATION")
        print(pd.read_sql_query(qualification_query, connection).to_string(index=False))


if __name__ == "__main__":
    analyse_unemployment()
