import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

# ---------------------------------------
# Load featured dataset
# ---------------------------------------
df = pd.read_csv("data/processed/eda_featured_data.csv")

# Target
y = df["processing_time_days"]

# Drop non ML columns
X = df.drop(columns=["processing_time_days", "source_file", "month", "year"])

print("Dataset Shape:", X.shape)

# ---------------------------------------
# Train Test Split
# ---------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# Linear Regression (Baseline)
# ---------------------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)

lr_preds = lr.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_preds)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_preds))
lr_r2 = r2_score(y_test, lr_preds)

print("\nLinear Regression Results:")
print("MAE:", lr_mae)
print("RMSE:", lr_rmse)
print("R2:", lr_r2)

# ---------------------------------------
# Random Forest
# ---------------------------------------
rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=12,
    random_state=42
)

rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_preds)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))
rf_r2 = r2_score(y_test, rf_preds)

print("\nRandom Forest Results:")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R2:", rf_r2)

# ---------------------------------------
# Select Best Model
# ---------------------------------------
best_model = rf if rf_r2 > lr_r2 else lr

os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.pkl")

print("\nBest model saved successfully.")

# ---------------------------------------
# Feature Importance (Random Forest)
# ---------------------------------------
importance = pd.Series(rf.feature_importances_, index=X.columns)
print("\nTop Important Features:")
print(importance.sort_values(ascending=False).head(10))
