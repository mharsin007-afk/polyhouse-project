import json
from pathlib import Path

import joblib
import pandas as pd

from logger import log_prediction
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


def predict_yield(*args, **kwargs) -> float:
    """
    Supports two calling styles:

    New style:
        predict_yield(temperature_c, humidity_pct, co2_ppm)

    Old style:
        predict_yield(
            model,
            scaler,
            feature_cols,
            temperature_c,
            humidity_pct,
            co2_ppm
        )
    """

    # New style: predict_yield(temp, humidity, co2)
    if len(args) == 3:
        model, scaler, feature_cols = load_artifacts()
        temperature_c, humidity_pct, co2_ppm = args

    # Old style: predict_yield(model, scaler, feature_cols, temp, humidity, co2)
    elif len(args) == 6:
        (
            model,
            scaler,
            feature_cols,
            temperature_c,
            humidity_pct,
            co2_ppm,
        ) = args

    # Keyword arguments
    elif kwargs:
        if {"model", "scaler", "feature_cols"}.issubset(kwargs):
            model = kwargs["model"]
            scaler = kwargs["scaler"]
            feature_cols = kwargs["feature_cols"]
        else:
            model, scaler, feature_cols = load_artifacts()

        temperature_c = kwargs["temperature_c"]
        humidity_pct = kwargs["humidity_pct"]
        co2_ppm = kwargs["co2_ppm"]

    else:
        raise TypeError(
            "predict_yield expects either "
            "(temperature_c, humidity_pct, co2_ppm) "
            "or "
            "(model, scaler, feature_cols, temperature_c, humidity_pct, co2_ppm)"
        )

    row = pd.DataFrame(
        {
            "temperature_c": [temperature_c],
            "humidity_pct": [humidity_pct],
            "co2_ppm": [co2_ppm],
        }
    )

    row = row[feature_cols]

    scaled = scaler.transform(row)

    scaled_df = pd.DataFrame(
        scaled,
        columns=feature_cols,
    )

    prediction = float(model.predict(scaled_df)[0])

    try:
        log_prediction(
            temperature_c,
            humidity_pct,
            co2_ppm,
            prediction,
        )
    except Exception as e:
        print(f"Logging failed: {e}")

    return prediction


if __name__ == "__main__":
    print(predict_yield(15.0, 60.0, 900.0))
    print(predict_yield(22.0, 88.0, 900.0))
    print(predict_yield(30.0, 95.0, 900.0))