# 🍄 Polyhouse Sensor Project: Mushroom Yield Forecasting

## Live Demo

🌐 **Streamlit Application:** `polyhouse-project-9axvfnp2fyygwtz2yvcxfqPASTE_YOUR_STREAMLIT_URL_HERE`

---

## Project Overview

This project analyzes environmental sensor data collected from a mushroom polyhouse to forecast daily mushroom yield.

The system monitors key growing conditions such as temperature, humidity, and CO₂ concentration and uses machine learning to estimate yield under different environmental scenarios.

The project demonstrates an end-to-end machine learning workflow, including data ingestion, cleaning, exploratory analysis, feature engineering, model training, validation, testing, and cloud deployment.

---

## Project Goal

Develop a decision-support tool for controlled-environment mushroom cultivation by predicting daily yield from polyhouse sensor readings.

---

## Dataset

The dataset contains time-series sensor readings collected from a mushroom polyhouse environment.

### Features

| Feature         | Description                        |
| --------------- | ---------------------------------- |
| `timestamp`     | Sensor observation timestamp       |
| `temperature_c` | Temperature (°C)                   |
| `humidity_pct`  | Relative humidity (%)              |
| `co2_ppm`       | Carbon dioxide concentration (ppm) |
| `yield_kg`      | Daily mushroom yield (kg)          |

---

## Live Prediction Example

| Temperature (°C) | Humidity (%) | CO₂ (ppm) | Predicted Yield (kg) |
| ---------------- | ------------ | --------- | -------------------- |
| 22               | 88           | 920       | 17.00                |

---

## Project Structure

```text
polyhouse-project/
├── .streamlit/
│   └── config.toml
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── models/
│   ├── feature_cols.json
│   ├── minmax_scaler_train.joblib
│   └── random_forest_tuned.joblib
├── reports/
│   ├── figures/
│   ├── data_quality.md
│   ├── eda_notes.md
│   ├── metrics_linear.md
│   ├── model_comparison.csv
│   └── test_scenarios.md
├── src/
│   ├── ingest.py
│   ├── clean.py
│   ├── eda.py
│   ├── features.py
│   ├── split_scale.py
│   ├── train_linear.py
│   ├── train_random_forest.py
│   ├── grid_search_rf.py
│   ├── cross_validation.py
│   ├── model_comparison.py
│   └── predict.py
├── tests/
│   └── test_predict.py
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## Machine Learning Pipeline

```text
Raw CSV Data
      ↓
Data Ingestion
      ↓
Data Quality Assessment
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Chronological Train/Test Split
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Cross-Validation & Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Streamlit Deployment
```

---

## Data Cleaning Rules

| Feature       | Valid Range          |
| ------------- | -------------------- |
| temperature_c | 10–35 °C             |
| humidity_pct  | 50–100 %             |
| co2_ppm       | 400–2000 ppm         |
| yield_kg      | Positive values only |

Cleaning steps included:

* Missing value analysis
* Forward filling sensor gaps
* Duplicate removal
* Range validation
* Invalid observation filtering

---

## Feature Engineering

### Input Features

* `temperature_c`
* `humidity_pct`
* `co2_ppm`

### Engineered Feature

```text
temp_humid_interaction = temperature_c × humidity_pct / 100
```

### Target Variable

```text
yield_kg
```

---

## Train/Test Strategy

To prevent data leakage, the dataset was sorted chronologically before splitting.

* Training set: 292 rows (80%)
* Test set: 73 rows (20%)

### Training Period

2024-01-01 → 2024-10-18

### Testing Period

2024-10-19 → 2024-12-30

A `MinMaxScaler` was fitted only on the training data and reused for test and deployment data.

---

## Model Development

The following models were evaluated:

* Linear Regression
* Random Forest Regressor
* Tuned Random Forest Regressor

### Champion Model

**Tuned Random Forest Regressor**

Best hyperparameters:

```text
max_depth = 8
min_samples_leaf = 5
n_estimators = 100
```

---

## Model Performance

| Metric    | Value    |
| --------- | -------- |
| Test MAE  | 0.445 kg |
| Test RMSE | 0.562 kg |
| Test R²   | 0.369    |

---

## Validation Scenarios

| Scenario           | Temperature | Humidity | CO₂      | Predicted Yield |
| ------------------ | ----------- | -------- | -------- | --------------- |
| Optimal            | 22°C        | 88%      | 920 ppm  | 17.00 kg        |
| Dry Spell          | 22°C        | 60%      | 920 ppm  | 16.94 kg        |
| Heat Spike         | 32°C        | 88%      | 920 ppm  | 18.16 kg        |
| Extreme CO₂        | 22°C        | 88%      | 1800 ppm | 16.76 kg        |
| Multiple Stressors | 32°C        | 60%      | 1800 ppm | 18.05 kg        |

Streamlit and CLI predictions matched exactly across all validation scenarios.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mharsin007-afk/polyhouse-project.git
cd polyhouse-project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Run Inference

```python
from src.predict import predict_yield

prediction = predict_yield(
    22.0,
    88.0,
    920.0
)

print(f"Predicted Yield: {prediction:.2f} kg")
```

---

## Run Tests

```bash
python -m pytest tests/
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib
* Git
* GitHub

---

## Future Improvements

* Integrate real-time sensor streaming
* Add automated model retraining
* Improve biological calibration with larger datasets
* Add user authentication and role-based access
* Deploy model monitoring dashboards

```
```
