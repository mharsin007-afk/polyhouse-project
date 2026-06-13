import pandas as pd
import matplotlib.pyplot as plt

from joblib import load

# Load test data
test = pd.read_csv("data/processed/test.csv")

X_test = test.drop(columns=["timestamp", "yield_kg"])
y_test = test["yield_kg"]

# Champion model
champion = load("models/random_forest_tuned.joblib")

pred = champion.predict(X_test)

# Comparison table
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "Tuned Random Forest"
    ],
    "CV_MAE": [
        0.440,
        0.474,
        0.465
    ],
    "Test_MAE": [
        0.470,
        0.449,
        0.445
    ],
    "RMSE": [
        0.592,
        0.580,
        0.562
    ],
    "R2": [
        0.289,
        0.328,
        0.369
    ],
    "Interpretability": [
        "High",
        "Medium",
        "Medium-Low"
    ]
})

print(results.to_markdown(index=False))

results.to_csv(
    "reports/model_comparison.csv",
    index=False
)

# Predicted vs Actual
plt.figure(figsize=(6,6))

plt.scatter(y_test, pred, alpha=0.6)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Champion Model: Predicted vs Actual")

plt.tight_layout()

plt.savefig(
    "reports/figures/pred_vs_actual.png",
    dpi=150
)

print("\nSaved:")
print("reports/model_comparison.csv")
print("reports/figures/pred_vs_actual.png")