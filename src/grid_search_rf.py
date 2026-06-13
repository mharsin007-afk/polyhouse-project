import pandas as pd
import numpy as np
import json
import time
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Start timer
start_time = time.time()

# Load datasets
train = pd.read_csv("data/processed/train.csv")
test = pd.read_csv("data/processed/test.csv")

# Features and target
X_train = train.drop(columns=["timestamp", "yield_kg"])
y_train = train["yield_kg"]

X_test = test.drop(columns=["timestamp", "yield_kg"])
y_test = test["yield_kg"]

# TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)

# Parameter grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5],
}

# Base model
rf = RandomForestRegressor(
    random_state=42,
    n_jobs=-1
)

# Grid Search
search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True
)

search.fit(X_train, y_train)

# Best results
print("Best Parameters:")
print(search.best_params_)

print(f"\nBest CV MAE: {-search.best_score_:.3f}")

best_model = search.best_estimator_

# Test evaluation
pred = best_model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("\nTuned Model Test Results")
print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")

# Save best params
with open("models/rf_best_params.json", "w") as f:
    json.dump(search.best_params_, f, indent=2)

# Save model
joblib.dump(
    best_model,
    "models/random_forest_tuned.joblib"
)

# Save CV results
cv_results = pd.DataFrame(search.cv_results_)
cv_results.to_csv(
    "reports/grid_search_cv_results.csv",
    index=False
)

# Runtime
runtime = time.time() - start_time

print(f"\nRuntime: {runtime:.2f} seconds")