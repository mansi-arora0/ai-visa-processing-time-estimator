# AI-Enabled Visa Status Prediction & Processing Time Estimator  
## Milestone 1: Data Collection & Preprocessing

---

## 📌 Project Overview

This project focuses on building an AI-based system to analyze and predict visa application processing times using publicly available immigration data.  
Milestone 1 concentrates on collecting real-world visa data, cleaning it, and preparing a structured dataset suitable for machine learning models.

The dataset is sourced from monthly reports published by the **U.S. Citizenship and Immigration Services (USCIS)** under the Appropriations Reporting Requirement.

---

## 🎯 Milestone 1 Objective

Build a clean, structured, and machine-learning-ready dataset for visa processing time prediction.

---

## 📂 Dataset Source

- **Source:** USCIS Immigration and Citizenship Data Library  
- **Report Type:** Appropriations Reporting Requirement – Application Processing Data  
- **Time Period:** 2023–2025  
- **Format:** Monthly CSV files  
- **Access:** Public government data (no personal or sensitive information)

---

## 🛠️ Tasks Completed

### 1. Data Collection
- Collected 23 monthly USCIS CSV files.
- Data includes multiple visa forms such as I-130, I-485, I-765, N-400, etc.

### 2. Data Cleaning & Preprocessing
- Removed report headers, metadata, and notes.
- Standardized column names.
- Cleaned numeric fields containing commas.
- Merged all monthly CSV files into a single dataset.
- Added a `source_file` column to retain month/year context.

### 3. Target Variable Creation
- USCIS reports average processing time in months.
- Converted processing time to days using:
  
  processing_time_days = avg_processing_time × 30

- This column is used as the target variable for prediction.

### 4. Missing Value Handling
- Dropped rows with missing target values.
- Filled missing categorical values where required.
- Final dataset contains zero missing values.

### 5. Categorical Encoding
- Encoded categorical variables (`form_number`, `description`) using Label Encoding for machine learning compatibility.

---

## 📊 Final Dataset Description

**File Path:**
- data/processed/clean_uscis_processing_data.csv

**Dataset Shape:**  
- Rows: 556  
- Columns: 9  

| Column Name | Description |
|------------|------------|
| form_number | Encoded visa form type |
| description | Encoded application description |
| forms_received | Number of applications received |
| approvals | Number of approved applications |
| denials | Number of denied applications |
| pending | Total pending applications |
| pending_over_6_months | Applications pending over six months |
| processing_time_days | Target variable (processing time in days) |
| source_file | Original monthly CSV file name |
---

## ✅ Milestone 1 Status

- Data collected  
- Data cleaned and merged  
- Target variable generated  
- Missing values handled  
- Dataset ready for modeling  

**Milestone 1 successfully completed.**

---



