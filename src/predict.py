import json
from pathlib import Path

import joblib
import pandas as pd

MODEL_DIR = Path("models")


def load_artifacts():
    scaler = joblib.load(
        MODEL_DIR / "minmax_scaler_train.joblib"
    )

    model = joblib.load(
        MODEL_DIR / "random_forest_tuned.joblib"
    )

    feature_cols = json.loads(
        (MODEL_DIR / "feature_cols.json").read_text()
    )

    return model, scaler, feature_cols


def predict_yield(
    model,
    scaler,
    feature_cols,
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    row = pd.DataFrame(
        {
            "temperature_c": [temperature_c],
            "humidity_pct": [humidity_pct],
            "co2_ppm": [co2_ppm]
        }
    )

    row = row[feature_cols]

    scaled = scaler.transform(row)

    scaled_df = pd.DataFrame(
        scaled,
        columns=feature_cols
    )

    prediction = model.predict(scaled_df)

    return float(prediction[0])
if __name__ == "__main__":
    model, scaler, feature_cols = load_artifacts()

    print(
        predict_yield(
            model,
            scaler,
            feature_cols,
            temperature_c=15.0,
            humidity_pct=60.0,
            co2_ppm=900.0
        )
    )

    print(
        predict_yield(
            model,
            scaler,
            feature_cols,
            temperature_c=22.0,
            humidity_pct=88.0,
            co2_ppm=900.0
        )
    )

    print(
        predict_yield(
            model,
            scaler,
            feature_cols,
            temperature_c=30.0,
            humidity_pct=95.0,
            co2_ppm=900.0
        )
    )
