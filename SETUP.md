
# Setup Guide

## SA Employment Insights

This guide explains how to run the Data Engineering
project on a Windows computer using VS Code.

## Requirements

- Python 3
- Git
- Visual Studio Code

## 1. Clone the Repository

Open a PowerShell terminal:

```powershell
git clone https://github.com/Bongiswa025/sa-unemployment-data-pipeline.git
cd sa-unemployment-data-pipeline
```

## 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## 4. Run the Data Pipeline

```powershell
python run_pipeline.py
```

The pipeline will:

1. Extract the CSV data.
2. Clean and transform the records.
3. Load the data into SQLite.
4. Generate unemployment summaries.

## 5. Run Automated Tests

```powershell
python -m unittest discover -s tests -v
```

The project currently includes nine automated tests.

Run the pipeline before running the tests because
the tests check generated data files.

## 6. Launch the Dashboard

```powershell
python -m streamlit run dashboard/app.py
```

Open the local URL displayed in the terminal,
usually http://localhost:8501.

## 7. Stop the Dashboard

Press Ctrl + C in the terminal.

## Important Note

The dataset contains fictional sample records for
educational purposes. It does not represent official
South African unemployment statistics.
