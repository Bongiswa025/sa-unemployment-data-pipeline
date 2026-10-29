
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

# Display dataset
st.subheader("Unemployment Records")
st.dataframe(data, use_container_width=True)
