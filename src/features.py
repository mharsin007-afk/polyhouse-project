import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

"""
Features:
- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction = temperature_c * humidity_pct / 100

Target:
- yield_kg
"""

# Load cleaned data
df = pd.read_parquet(
    "data/interim/02_cleaned.parquet"
).sort_values("timestamp")

# Feature engineering
df["temp_humid_interaction"] = (
    df["temperature_c"]
    * df["humidity_pct"]
    / 100
)

# Feature list
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

# Features and target
X = df[feature_cols]
y = df["yield_kg"]

# Validation checks
print("X shape:", X.shape)
print("y shape:", y.shape)

# Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(
    scaler,
    "models/minmax_scaler.joblib"
)

# Create processed dataframe
processed = pd.DataFrame(
    X_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

processed["yield_kg"] = y.values

# Check for missing values
print("\nMissing values:")
print(processed.isna().sum())

# Verify scaling
print("\nMin values:")
print(processed.min())

print("\nMax values:")
print(processed.max())

# Save processed features
processed.to_parquet(
    "data/processed/features.parquet",
    index=False
)

print("\nFeature engineering completed successfully.")