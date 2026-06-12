import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load data
train = pd.read_csv("data/processed/train.csv")
test = pd.read_csv("data/processed/test.csv")

# Remove timestamp column
X_train = train.drop(columns=["timestamp", "yield_kg"])
y_train = train["yield_kg"]

X_test = test.drop(columns=["timestamp", "yield_kg"])
y_test = test["yield_kg"]

# Train model
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

# Predictions
pred = rf.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("\nRandom Forest Results")
print(f"MAE: {mae:.3f} kg")
print(f"RMSE: {rmse:.3f} kg")
print(f"R²: {r2:.3f}")

# Feature Importance Plot
plt.figure(figsize=(6,4))

labels = X_train.columns
importances = rf.feature_importances_

plt.barh(labels, importances)
plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()

plt.savefig(
    "reports/figures/rf_importance.png",
    dpi=150
)

# Save model
joblib.dump(
    rf,
    "models/random_forest.joblib"
)

print("\nModel saved to models/random_forest.joblib")
print("Feature importance plot saved.")