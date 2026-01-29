
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import matplotlib.pyplot as plt

# ---------------------------------------
# Load featured dataset
# ---------------------------------------
df = pd.read_csv("data/processed/eda_featured_data.csv")

# Target
y = df["processing_time_days"]

# Features
X = df.drop(columns=["processing_time_days", "source_file", "month", "year"])

print("Dataset Shape:", X.shape)

# ---------------------------------------
# Train Test Split
# ---------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# Models
# ---------------------------------------

lr = LinearRegression()
ridge = Ridge(alpha=1.0)
rf = RandomForestRegressor(n_estimators=200, max_depth=12, random_state=42)
gbr = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05)
etr = ExtraTreesRegressor(n_estimators=300, random_state=42)

models = {
    "Linear": lr,
    "Ridge": ridge,
    "RandomForest": rf,
    "GradientBoosting": gbr,
    "ExtraTrees": etr
}

scores = {}

# ---------------------------------------
# Train + Evaluate All Models
# ---------------------------------------

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    scores[name] = r2

    print(f"\n{name} Results:")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2:", r2)

# ---------------------------------------
# Select Best Model Automatically
# ---------------------------------------

best_name = max(scores, key=scores.get)
best_model = models[best_name]

os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.pkl")

print("\nBest Model:", best_name)
print("Best model saved successfully.")

# ---------------------------------------
# Feature Importance (Tree Models Only)
# ---------------------------------------

if hasattr(best_model, "feature_importances_"):
    importance = pd.Series(best_model.feature_importances_, index=X.columns)

    os.makedirs("outputs/model_plots", exist_ok=True)

    importance.sort_values().plot(kind="barh", figsize=(8,6))
    plt.title("Feature Importance")
    plt.xlabel("Importance Score")
    plt.savefig("outputs/model_plots/feature_importance.png", dpi=300, bbox_inches="tight")
    plt.show()

# ---------------------------------------
# Actual vs Predicted Plot
# ---------------------------------------

best_preds = best_model.predict(X_test)

plt.figure(figsize=(6,5))
plt.scatter(y_test, best_preds, alpha=0.7)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         "--r")

plt.xlabel("Actual Processing Time")
plt.ylabel("Predicted Processing Time")
plt.title("Actual vs Predicted")

plt.savefig("outputs/model_plots/actual_vs_predicted.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------------------
# Model Comparison Plot
# ---------------------------------------

plt.figure(figsize=(7,5))
plt.bar(scores.keys(), scores.values())
plt.ylabel("R2 Score")
plt.title("Model Comparison")
plt.xticks(rotation=30)

plt.savefig("outputs/model_plots/model_comparison.png", dpi=300)
plt.show()

print("\nModel comparison plot saved.")
