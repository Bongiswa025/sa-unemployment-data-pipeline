
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "unemployment.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "cleaned_unemployment.csv"


def transform_data():
    # Read our original CSV file
    data = pd.read_csv(INPUT_FILE)

    print("Original number of records:", len(data))

    # Remove duplicate records
    data = data.drop_duplicates()

    # Remove rows with missing important information
    data = data.dropna(
        subset=["province", "age", "qualification", "employment_status"]
    )

    # Convert ages to numbers
    data["age"] = pd.to_numeric(data["age"], errors="coerce")

    # Remove invalid ages
    data = data.dropna(subset=["age"])
    data = data[data["age"].between(15, 100)].copy()

    # Create age categories
    data["age_group"] = pd.cut(
        data["age"],
        bins=[14, 24, 34, 44, 54, 64, 100],
        labels=["15-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    )

    # Save cleaned data
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT_FILE, index=False)

    print("Cleaned number of records:", len(data))
    print("Cleaned data saved successfully!")
    print(data.head())


if __name__ == "__main__":
    transform_data()
