import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from pathlib import Path

# Load cleaned dataset
df = pd.read_parquet("data/interim/02_cleaned.parquet")

# Sort chronologically
df = df.sort_values("timestamp")

# Features and target
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

target_col = "yield_kg"

# 80/20 chronological split
split_idx = int(len(df) * 0.8)

print("Split Index:", split_idx)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

# Verify no leakage
assert (
    test["timestamp"].min()
    > train["timestamp"].max()
)

print("\n✓ No data leakage detected")

# Scale using train statistics only
scaler = MinMaxScaler()

X_train = scaler.fit_transform(
    train[feature_cols]
)

X_test = scaler.transform(
    test[feature_cols]
)

# Target arrays
y_train = train[target_col].values
y_test = test[target_col].values

# Shape checks
print("\nFeature Shapes")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

print("\nTarget Shapes")
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

# Save split artifacts
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

train.to_csv(
    "data/processed/train.csv",
    index=False
)

test.to_csv(
    "data/processed/test.csv",
    index=False
)

print("\n✓ Train/Test CSV files saved")

# Save scaler
Path("models").mkdir(
    exist_ok=True
)

joblib.dump(
    scaler,
    "models/minmax_scaler_train.joblib"
)

print("✓ Scaler saved")

# Split summary
print("\nTrain Rows:", len(train))
print("Test Rows:", len(test))

print("\nTrain Date Range:")
print(train["timestamp"].min(), "→", train["timestamp"].max())

print("\nTest Date Range:")
print(test["timestamp"].min(), "→", test["timestamp"].max())