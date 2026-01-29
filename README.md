# AI-Enabled Visa Status Prediction & Processing Time Estimator  

## Milestone 1 & Milestone 2 Progress

---

## Project Overview

This project focuses on building an AI-based system to analyze and predict visa application processing times using publicly available immigration data.  
The goal is to understand patterns in visa processing, identify key influencing factors, and develop predictive models for processing time estimation.

The dataset is sourced from monthly reports published by the **U.S. Citizenship and Immigration Services (USCIS)** under the Appropriations Reporting Requirement.

---

## Dataset Source

- **Source:** USCIS Immigration and Citizenship Data Library  
- **Report Type:** Appropriations Reporting Requirement – Application Processing Data  
- **Time Period:** 2023–2025  
- **Format:** Monthly CSV files  
- **Access:** Public government data (no personal or sensitive information)

---

# Milestone 1: Data Collection & Preprocessing

### Objective  
Build a clean, structured, and machine-learning-ready dataset for visa processing time prediction.

---

## Tasks Completed

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


### 4. Missing Value Handling
- Dropped rows with missing target values.
- Filled missing categorical values where required.
- Final dataset contains zero missing values.

### 5. Categorical Encoding
- Encoded categorical variables (`form_number`, `description`) using Label Encoding for machine learning compatibility.

---

## Final Dataset (Milestone 1)

**File Path:**  
`data/processed/clean_uscis_processing_data.csv`

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

## Milestone 1 Status  
**Completed Successfully**

---

# Milestone 2: Exploratory Data Analysis & Feature Engineering

### 🎯 Objective  
Analyze the dataset, identify patterns, visualize trends, and engineer new features to improve model performance.

---

## Tasks Completed

### 1. Exploratory Data Analysis (EDA)

- Visualized distribution of visa processing times  
- Analyzed relationship between pending cases and processing time  
- Generated correlation heatmap for all numeric features  

**Visualizations Created:**
- Processing Time Distribution
- Pending vs Processing Time Scatter Plot
- Feature Correlation Heatmap

**Saved in:**  
`outputs/plots/`

---

### 2. Key Insights

- Processing times vary significantly across different visa forms  
- Higher pending case volume does **not always** mean longer processing time  
- Strong correlations exist between:
- Forms received & approvals  
- Pending & pending over 6 months  
- Processing time shows moderate correlation with application type (description)

---

### 3. Feature Engineering

New features were created to enhance predictive power:

| Feature | Description |
|--------|-------------|
| month | Extracted month from source file |
| year | Extracted year from source file |
| seasonal_index | Average processing time per month |
| form_avg_processing_time | Average processing time per form type |
| backlog_ratio | pending / forms_received |

---

## Milestone 2 Output

**File Path:**  
`data/processed/eda_featured_data.csv`

This dataset includes:
- Original cleaned features  
- Newly engineered features  
- Ready for ML modeling  

---

## Milestone 2 Status  
**Completed Successfully**

---

## 👩‍💻 Author

**Mansi**  
Infosys Springboard Internship
Project: *AI-Enabled Visa Status Prediction and Processing Time Estimator*




