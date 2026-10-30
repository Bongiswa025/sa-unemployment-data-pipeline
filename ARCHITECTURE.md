
# Project Architecture

## SA Employment Insights

This project demonstrates an ETL (Extract, Transform, Load)
pipeline for analysing fictional South African unemployment
records.

## Data Flow

```text
Sample CSV Dataset
        |
        v
Extract (src/extract.py)
        |
        v
Transform (src/transform.py)
        |
        v
Cleaned CSV Dataset
        |
        v
Load (src/load.py)
        |
        v
SQLite Database
        |
        +--------------------+
        |                    |
        v                    v
SQL Analysis           Streamlit Dashboard
(src/analysis.py)      (dashboard/app.py)
                             |
                             v
                    Filters, Charts, CSV Export
```

## Components

### Extraction

Reads source data from `data/raw/unemployment.csv`.

### Transformation

Cleans the records, validates ages and creates age groups.

### Loading

Stores processed records in the SQLite database.

### Analysis

Groups unemployment records by province, age group and
qualification.

### Dashboard

Provides interactive filters, charts, summary metrics
and downloadable CSV results.

### Pipeline Runner

`run_pipeline.py` executes the four pipeline stages
in the correct order.

### Automated Testing

The project includes tests for data quality, database
integrity and pipeline execution.

## Limitations

The current dataset contains 10 fictional records.
The project is a demonstration and does not provide
official unemployment statistics or real job-seeker
matching.
