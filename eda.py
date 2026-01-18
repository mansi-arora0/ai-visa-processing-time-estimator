# Load your cleaned dataset 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder to store plots
os.makedirs("outputs/plots", exist_ok=True)

df = pd.read_csv("data/processed/clean_uscis_processing_data.csv")

# Basic info
print(df.shape)
print(df.info())
print(df.describe())

# -------------------------------
# 1. Distribution of Processing Time
# -------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["processing_time_days"], bins=30, kde=True)
plt.title("Distribution of Visa Processing Time (Days)")
plt.xlabel("Processing Time (Days)")
plt.ylabel("Count")

plt.savefig("outputs/plots/processing_time_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 2. Pending vs Processing Time
# -------------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x=df["pending"], y=df["processing_time_days"])
plt.title("Pending Applications vs Processing Time")
plt.xlabel("Pending Cases")
plt.ylabel("Processing Time (Days)")

plt.savefig("outputs/plots/pending_vs_processing_time.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 3. Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8,6))
corr = df.drop(columns=["source_file"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")

plt.savefig("outputs/plots/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# Feature Engineering
# -------------------------------
df["month"] = df["source_file"].str.extract(
    r'(january|february|march|april|may|june|july|august|september|october|november|december)',
    expand=False
)

df["year"] = df["source_file"].str.extract(r'(20\d{2})')

seasonal_avg = df.groupby("month")["processing_time_days"].mean()
df["seasonal_index"] = df["month"].map(seasonal_avg)

form_avg = df.groupby("form_number")["processing_time_days"].mean()
df["form_avg_processing_time"] = df["form_number"].map(form_avg)

df["backlog_ratio"] = df["pending"] / (df["forms_received"] + 1)

# Save Milestone 2 dataset
df.to_csv("data/processed/eda_featured_data.csv", index=False)

print("✅ Milestone 2 dataset saved successfully.")
print("📊 Plots saved in outputs/plots/")

