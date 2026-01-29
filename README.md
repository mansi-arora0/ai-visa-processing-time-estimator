# AI-Enabled Visa Status Prediction & Processing Time Estimator  
---

## Project Overview

This project builds an end-to-end machine learning pipeline to analyze and predict visa application processing times using real-world public immigration data.

The system performs:

- Data ingestion from government CSV reports  
- Data preprocessing and feature engineering  
- Exploratory Data Analysis (EDA) with visual insights  
- Regression modeling to predict processing time  
- Model evaluation and selection  
- Saving trained models for future deployment  

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
Build a clean, structured, machine-learning-ready dataset.

---

## Tasks Completed

### Data Collection
- Collected 23 monthly USCIS CSV files.
- Includes multiple visa forms (I-130, I-485, I-765, N-400, etc.).

### Data Cleaning & Preprocessing
- Removed report headers and notes.
- Standardized column names.
- Cleaned numeric fields.
- Merged all monthly CSVs into one dataset.
- Added `source_file` for month/year traceability.

### Target Variable Creation

USCIS reports processing time in months.  
Converted to days:

processing_time_days = avg_processing_time × 30


### Missing Value Handling
- Dropped rows with missing targets.
- Filled categorical missing values.
- Final dataset contains **zero missing values**.

### Categorical Encoding
- Encoded `form_number` and `description` using Label Encoding.

---

## Milestone 1 Output

**File:**  
`data/processed/clean_uscis_processing_data.csv`

**Dataset Shape:**  
- Rows: 556  
- Columns: 9  

---

## Milestone 1 Status  
  Completed Successfully

---

# Milestone 2: Exploratory Data Analysis & Feature Engineering

### 🎯 Objective  
Analyze patterns, visualize trends, and engineer predictive features.

---

## EDA Performed

Visualizations created:

- Processing Time Distribution  
- Pending vs Processing Time  
- Feature Correlation Heatmap  

Saved under:

outputs/plots/

---

## Key Insights

- Processing times vary significantly across visa types.
- Pending volume alone does not always imply longer processing.
- Strong correlations observed between:
  - Forms received ↔ approvals  
  - Pending ↔ pending over 6 months  
- Processing time moderately correlates with application type.

---

## Feature Engineering

Additional features created:

| Feature | Description |
|--------|-------------|
| month | Extracted from source file |
| year | Extracted from source file |
| seasonal_index | Avg processing time per month |
| form_avg_processing_time | Avg per visa form |
| backlog_ratio | pending / forms_received |

---

## Milestone 2 Output

**File:**  
`data/processed/eda_featured_data.csv`

Includes original + engineered features.

---

## Milestone 2 Status  
Completed Successfully

---

# Milestone 3: Predictive Modeling

### 🎯 Objective  
Train regression models to predict visa processing time and select the best model.

---

## Models Implemented

- Linear Regression (baseline)
- Ridge Regression
- Random Forest Regressor

---

## Evaluation Metrics Used

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Model Performance (Best Model: Random Forest)

- **MAE:** ~29 days  
- **RMSE:** ~61 days  
- **R² Score:** ~0.91  

Random Forest significantly outperformed linear models.

---

## Feature Importance (Top Contributors)

- Backlog Ratio  
- Form Average Processing Time  
- Forms Received  
- Description  
- Approvals  

This shows backlog and historical form behavior are strong predictors.

---

## Visualizations Created

Saved under:

outputs/model_plots/


- Feature Importance Plot  
- Actual vs Predicted Processing Time  
- Model Comparison Chart  

---

## Model Saving

Best performing model saved as:

models/best_model.pkl


Ready for deployment or API integration.

---

## Milestone 3 Status  
Completed Successfully

---

# Next Steps (Planned)

- Build Flask/FastAPI inference API  
- Create simple frontend UI  
- Add model versioning  
- Deployment (Render / HuggingFace / Streamlit)  

---

## Author

**Mansi**  
Infosys Springboard Internship  
Project: *AI-Enabled Visa Status Prediction and Processing Time Estimator*

---






