
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "unemployment.db"

st.set_page_config(
    page_title="SA Employment Insights",
    page_icon="📊",
    layout="wide"
)

st.title("🇿🇦 SA Employment Insights Dashboard")
st.write("Explore unemployment records by province, age and qualification.")

st.info("Demo: This dashboard uses fictional sample data, not official South African unemployment statistics.")

if not DATABASE_FILE.exists():
    st.error("Database not found. Run the ETL scripts first.")
    st.stop()

with sqlite3.connect(DATABASE_FILE) as connection:
    data = pd.read_sql_query(
        "SELECT * FROM unemployment",
        connection
    )

# Only analyse unemployed records
data = data[data["employment_status"] == "Unemployed"].copy()


# Dashboard filters
st.sidebar.header("Filter Unemployment Data")

# Province filter
province_options = ["All"] + sorted(data["province"].dropna().unique().tolist())
selected_province = st.sidebar.selectbox("Select Province", province_options)

# Age group filter
age_options = ["All"] + sorted(data["age_group"].dropna().unique().tolist())
selected_age = st.sidebar.selectbox("Select Age Group", age_options)

# Gender filter
gender_options = ["All"] + sorted(data["gender"].dropna().unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Qualification filter
qualification_options = ["All"] + sorted(
    data["qualification"].dropna().unique().tolist()
)
selected_qualification = st.sidebar.selectbox(
    "Select Qualification", qualification_options
)

# Apply selected filters
if selected_province != "All":
    data = data[data["province"] == selected_province]

if selected_age != "All":
    data = data[data["age_group"] == selected_age]

if selected_gender != "All":
    data = data[data["gender"] == selected_gender]

if selected_qualification != "All":
    data = data[data["qualification"] == selected_qualification]


# Summary statistics
total = len(data)
provinces = data["province"].nunique()
qualifications = data["qualification"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Unemployed Records", total)
col2.metric("Provinces Represented", provinces)
col3.metric("Qualification Categories", qualifications)

st.divider()

# Unemployment by province
st.subheader("Unemployment by Province")

province_counts = data["province"].value_counts()
st.bar_chart(province_counts)

# Unemployment by age group
st.subheader("Unemployment by Age Group")

age_counts = data["age_group"].value_counts()
st.bar_chart(age_counts)

# Unemployment by qualification
st.subheader("Unemployment by Qualification")

qualification_counts = data["qualification"].value_counts()
st.bar_chart(qualification_counts)


# Unemployment by gender
st.subheader("Unemployment by Gender")

gender_counts = data["gender"].value_counts()
st.bar_chart(gender_counts)


# Display dataset
st.subheader("Unemployment Records")
st.dataframe(data, use_container_width=True)


# Download filtered unemployment records
st.subheader("Download Unemployment Data")

csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_unemployment_data.csv",
    mime="text/csv"
)

