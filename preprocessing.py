import pandas as pd
import glob
import os
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# 1. Locate raw CSV files
# --------------------------------------------------
DATA_PATH = "data/raw/*.csv"
files = glob.glob(DATA_PATH)

print(f"Number of CSV files found: {len(files)}")

if len(files) == 0:
    raise FileNotFoundError("No CSV files found in data/raw/")

# --------------------------------------------------
# 2. Read, clean headers, and merge monthly files
# --------------------------------------------------
df_list = []

for file in files:
    # Skip report text rows; real header starts at row 5
    temp_df = pd.read_csv(file, skiprows=4)

    # Remove footer rows like 'Notes'
    temp_df = temp_df[temp_df["Form Number"] != "Notes"]

    # Track source month/year
    temp_df["source_file"] = os.path.basename(file)

    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)
print("Merged dataset shape:", df.shape)

# --------------------------------------------------
# 3. Clean column names
# --------------------------------------------------
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
    .str.replace(".", "", regex=False)
)

print("Columns:", df.columns.tolist())

# --------------------------------------------------
# 4. Convert processing time (months → days)
# --------------------------------------------------
# USCIS reports Avg. Processing Time in MONTHS
df["processing_time_days"] = df["avg_processing_time"] * 30
df.drop(columns=["avg_processing_time"], inplace=True)

# --------------------------------------------------
# 5. Clean numeric columns (remove commas)
# --------------------------------------------------
numeric_cols = [
    "forms_received",
    "approvals",
    "denials",
    "pending",
    "pending_over_6_months",
    "processing_time_days"
]

for col in numeric_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

# --------------------------------------------------
# 6. Handle missing values
# --------------------------------------------------
# Drop rows where target is missing
df = df.dropna(subset=["processing_time_days"])

# Fill categorical missing values
df["description"] = df["description"].fillna("unknown")

print("Total missing values:", df.isnull().sum().sum())

# --------------------------------------------------
# 7. Encode categorical variables
# --------------------------------------------------
le = LabelEncoder()
df["form_number"] = le.fit_transform(df["form_number"])
df["description"] = le.fit_transform(df["description"])

# --------------------------------------------------
# 8. Save clean dataset (Milestone 1 output)
# --------------------------------------------------
os.makedirs("data/processed", exist_ok=True)

output_path = "data/processed/clean_uscis_processing_data.csv"
df.to_csv(output_path, index=False)

print("Milestone 1 dataset saved successfully.")
