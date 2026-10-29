
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "raw" / "unemployment.csv"


def extract_data():
    if not DATA_FILE.exists():
        print("Dataset not found:", DATA_FILE)
        return None

    data = pd.read_csv(DATA_FILE)

    print("Dataset loaded successfully!")
    print("Number of rows:", len(data))
    print("Columns:", list(data.columns))
    print(data.head())

    return data


if __name__ == "__main__":
    extract_data()
