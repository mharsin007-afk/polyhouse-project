import pandas as pd
import numpy as np

from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load TRAIN data only
train = pd.read_csv("data/processed/train.csv")

# Features and target
X = train.drop(columns=["timestamp", "yield_kg"])
y = train["yield_kg"]

# Time-series CV
tscv = TimeSeriesSplit(n_splits=3)

# Models
lr = LinearRegression()

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Cross-validation MAE
lr_scores = -cross_val_score(
    lr,
    X,
    y,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_scores = -cross_val_score(
    rf,
    X,
    y,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

print("\nLinear Regression CV MAE")
for i, score in enumerate(lr_scores, start=1):
    print(f"Fold {i}: {score:.3f}")

print(f"Mean CV MAE: {lr_scores.mean():.3f}")
print(f"Std Dev: {lr_scores.std():.3f}")

print("\nRandom Forest CV MAE")
for i, score in enumerate(rf_scores, start=1):
    print(f"Fold {i}: {score:.3f}")

print(f"Mean CV MAE: {rf_scores.mean():.3f}")
print(f"Std Dev: {rf_scores.std():.3f}")

# Train-vs-validation overfitting check
rf.fit(X, y)

train_pred = rf.predict(X)
train_mae = mean_absolute_error(y, train_pred)

print(f"\nRandom Forest Train MAE: {train_mae:.3f}")