
# Data Dictionary

## SA Employment Insights & Opportunity Matcher

This document describes the fields used in the
unemployment data pipeline.

## Dataset Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Unique identifier for each sample record |
| province | Text | South African province |
| age | Integer | Age in years |
| gender | Text | Gender recorded in the sample |
| qualification | Text | Highest qualification category |
| employment_status | Text | Employment status |
| age_group | Text | Age category created during transformation |

## Age Groups

The pipeline categorizes ages into:

- 15-24
- 25-34
- 35-44
- 45-54
- 55-64
- 65+

## Data Processing

1. Extract records from the source CSV.
2. Remove duplicates and incomplete records.
3. Validate ages.
4. Create the age_group column.
5. Save cleaned data to CSV.
6. Load the records into SQLite.
7. Analyze records by province, age and qualification.

## Data Source and Limitations

The current dataset contains 10 fictional sample records
created for educational testing.

These records are not official South African unemployment
statistics and must not be used to estimate unemployment
rates or identify real job seekers.

A future opportunity-matching feature would require
separately collected, voluntarily provided applicant data
and appropriate privacy protections.
