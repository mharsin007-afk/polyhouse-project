# src/predict.py

import json
from pathlib import Path

import joblib
import pandas as pd

MODEL_DIR = Path("models")

# Load deployment artifacts
_scaler = joblib.load(
    MODEL_DIR / "minmax_scaler_train.joblib"
)

_model = joblib.load(
    MODEL_DIR / "random_forest_tuned.joblib"
)

_feature_cols = json.loads(
    (MODEL_DIR / "feature_cols.json").read_text()
)


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:
    """
    Predict mushroom yield in kilograms.
    """

    # Create input row with correct feature names
    row = pd.DataFrame(
        {
            "temperature_c": [temperature_c],
            "humidity_pct": [humidity_pct],
            "co2_ppm": [co2_ppm]
        }
    )

    # Ensure correct column order
    row = row[_feature_cols]

    # Scale features
    scaled = _scaler.transform(row)

    # Preserve feature names after scaling
    scaled_df = pd.DataFrame(
        scaled,
        columns=_feature_cols
    )

    # Predict yield
    prediction = _model.predict(scaled_df)

    return float(prediction[0])


if __name__ == "__main__":

    prediction = predict_yield(
        temperature_c=22.0,
        humidity_pct=88.0,
        co2_ppm=920.0
    )

    print(
        f"Predicted Yield: {prediction:.2f} kg"
    )