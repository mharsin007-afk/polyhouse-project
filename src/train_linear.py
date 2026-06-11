import pandas as pd
import numpy as np
import json
import joblib
from pathlib import Path

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_parquet(
    "data/interim/02_cleaned.parquet"
)

df = df.sort_values("timestamp")

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

target_col = "yield_kg"

# ==================================================
# CHRONOLOGICAL TRAIN/TEST SPLIT
# ==================================================

split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

assert (
    test["timestamp"].min()
    > train["timestamp"].max()
)

print("✓ Chronological split verified")

# ==================================================
# SCALING
# ==================================================

scaler = MinMaxScaler()

X_train = scaler.fit_transform(
    train[feature_cols]
)

X_test = scaler.transform(
    test[feature_cols]
)

y_train = train[target_col].values
y_test = test[target_col].values

print("✓ Scaling completed")

# ==================================================
# TRAIN MODEL
# ==================================================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print("✓ Linear Regression trained")

# ==================================================
# PREDICTIONS
# ==================================================

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

# ==================================================
# METRICS
# ==================================================

train_mae = mean_absolute_error(
    y_train,
    pred_train
)

test_mae = mean_absolute_error(
    y_test,
    pred_test
)

train_rmse = np.sqrt(
    mean_squared_error(
        y_train,
        pred_train
    )
)

test_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        pred_test
    )
)

train_r2 = r2_score(
    y_train,
    pred_train
)

test_r2 = r2_score(
    y_test,
    pred_test
)

# ==================================================
# PRINT RESULTS
# ==================================================

print("\n========== LINEAR REGRESSION RESULTS ==========")

print("\nTRAIN METRICS")
print(f"MAE  : {train_mae:.3f} kg")
print(f"RMSE : {train_rmse:.3f} kg")
print(f"R²   : {train_r2:.3f}")

print("\nTEST METRICS")
print(f"MAE  : {test_mae:.3f} kg")
print(f"RMSE : {test_rmse:.3f} kg")
print(f"R²   : {test_r2:.3f}")

# ==================================================
# COEFFICIENTS
# ==================================================

print("\n========== FEATURE COEFFICIENTS ==========")

for feature, coef in zip(
    feature_cols,
    model.coef_
):
    direction = (
        "Positive"
        if coef > 0
        else "Negative"
    )

    print(
        f"{feature:<15} "
        f"{coef:>8.4f} "
        f"({direction})"
    )

print(
    f"\nIntercept: {model.intercept_:.4f}"
)

# ==================================================
# SAVE MODEL
# ==================================================

Path("models").mkdir(
    exist_ok=True
)

joblib.dump(
    model,
    "models/linear_regression.joblib"
)

print(
    "\n✓ Model saved -> models/linear_regression.joblib"
)

# ==================================================
# SAVE METRICS JSON
# ==================================================

Path("reports").mkdir(
    exist_ok=True
)

metrics = {
    "train_mae": float(train_mae),
    "train_rmse": float(train_rmse),
    "train_r2": float(train_r2),
    "test_mae": float(test_mae),
    "test_rmse": float(test_rmse),
    "test_r2": float(test_r2)
}

with open(
    "reports/metrics_linear.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

print(
    "✓ Metrics saved -> reports/metrics_linear.json"
)

# ==================================================
# SAVE MARKDOWN REPORT
# ==================================================

with open(
    "reports/metrics_linear.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Linear Regression Results\n\n")

    f.write("## Train Metrics\n")
    f.write(f"- MAE: {train_mae:.3f} kg\n")
    f.write(f"- RMSE: {train_rmse:.3f} kg\n")
    f.write(f"- R²: {train_r2:.3f}\n\n")

    f.write("## Test Metrics\n")
    f.write(f"- MAE: {test_mae:.3f} kg\n")
    f.write(f"- RMSE: {test_rmse:.3f} kg\n")
    f.write(f"- R²: {test_r2:.3f}\n\n")

    f.write("## Coefficients\n")

    for feature, coef in zip(
        feature_cols,
        model.coef_
    ):
        f.write(
            f"- {feature}: {coef:.4f}\n"
        )

print(
    "✓ Report saved -> reports/metrics_linear.md"
)

# ==================================================
# BASELINE COMMENT
# ==================================================

print("\n========== BASELINE ASSESSMENT ==========")

if test_r2 >= 0.8:
    print(
        "Excellent baseline model."
    )
elif test_r2 >= 0.6:
    print(
        "Good baseline model."
    )
elif test_r2 >= 0.4:
    print(
        "Reasonable baseline model."
    )
elif test_r2 >= 0:
    print(
        "Weak baseline model."
    )
else:
    print(
        "Negative R²: model performs worse than predicting the mean."
    )
# ==================================================
# DIAGNOSTICS
# ==================================================

import matplotlib.pyplot as plt

Path("reports/figures").mkdir(
    parents=True,
    exist_ok=True
)

# ------------------------------------------
# Residuals
# ------------------------------------------

train_residuals = y_train - pred_train
test_residuals = y_test - pred_test

print("\n========== DIAGNOSTICS ==========")

print(
    f"Train Residual Std: {train_residuals.std():.3f}"
)

print(
    f"Test Residual Std: {test_residuals.std():.3f}"
)

# ------------------------------------------
# Residuals vs Predicted
# ------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    pred_test,
    test_residuals,
    alpha=0.6
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.xlabel("Predicted Yield (kg)")
plt.ylabel("Residual (kg)")
plt.title("Residuals vs Predicted Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_vs_predicted_linear.png",
    dpi=150
)

plt.close()

# ------------------------------------------
# Residuals vs Humidity
# ------------------------------------------

humidity_test = X_test[:, 1]

plt.figure(figsize=(6,4))

plt.scatter(
    humidity_test,
    test_residuals,
    alpha=0.6
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.xlabel("Scaled Humidity")
plt.ylabel("Residual (kg)")
plt.title("Residuals vs Humidity")

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_vs_humidity_linear.png",
    dpi=150
)

plt.close()

print(
    "✓ Diagnostic plots saved -> reports/figures/"
)