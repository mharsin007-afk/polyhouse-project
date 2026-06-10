# Polyhouse Sensor Project

## Project Goal

The goal of this project is to monitor polyhouse environmental conditions for mushroom cultivation and analyze how factors such as temperature, humidity, and CO₂ concentration affect mushroom yield.

## Dataset

The dataset contains sensor readings collected from a mushroom polyhouse environment.

### Features

* Timestamp
* Temperature (°C)
* Humidity (%)
* CO₂ Concentration (ppm)
* Yield (kg)

## Project Structure

```text
polyhouse-project/
├── data/
│   ├── raw/
│   └── interim/
├── reports/
│   ├── figures/
│   ├── data_quality.md
│   └── eda_notes.md
├── src/
│   ├── ingest.py
│   ├── clean.py
│   └── eda.py
├── models/
└── README.md
```

## Project Pipeline

```text
Raw CSV Data
      ↓
Data Ingestion
      ↓
Data Quality Assessment
      ↓
Data Cleaning
      ↓
Cleaned Dataset
      ↓
Exploratory Data Analysis
      ↓
Visualizations & Insights
```

---

## Task 1: Data Ingestion

### Objective

Load raw sensor data and prepare it for processing.

### Work Completed

* Loaded CSV data using Pandas.
* Parsed timestamp values.
* Verified data types.
* Stored processed data in Parquet format.

### Output

* `src/ingest.py`
* `data/interim/01_loaded.parquet`

---

## Task 2: Data Quality Assessment & Data Cleaning

### Objective

Identify missing values, invalid sensor readings, and data quality issues before analysis.

### Data Quality Checks

The following checks were performed:

* Missing value analysis
* Data type verification
* Range validation
* Summary statistics generation
* Detection of invalid observations

### Cleaning Rules

| Column        | Valid Range          |
| ------------- | -------------------- |
| temperature_c | 10–35 °C             |
| humidity_pct  | 50–100 %             |
| co2_ppm       | ≥ 400 ppm            |
| yield_kg      | Positive values only |

### Work Completed

* Audited missing values.
* Removed invalid observations.
* Applied agritech-based validation rules.
* Generated a cleaned dataset.
* Documented null counts before and after cleaning.

### Outputs

* `src/clean.py`
* `reports/data_quality.md`
* `data/interim/02_cleaned.parquet`

---

## Task 3: Exploratory Data Analysis (EDA)

### Objective

Explore relationships between environmental variables and mushroom yield.

### Visualizations Generated

#### Correlation Heatmap

Analyzed correlations among:

* Temperature
* Humidity
* CO₂
* Yield

#### Scatter Plots

Generated scatter plots for:

* Humidity vs Yield
* Temperature vs Yield
* CO₂ vs Yield

### Key Findings

* Temperature showed the strongest positive correlation with yield.
* Humidity showed a moderate positive relationship with yield.
* CO₂ concentration showed a weak negative relationship with yield.

### Outputs

* `src/eda.py`
* `reports/eda_notes.md`
* `reports/figures/corr_heatmap.png`
* `reports/figures/scatter_yield.png`

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Parquet
* Git
* GitHub

---

## How to Run

### Data Ingestion

```bash
python src/ingest.py
```

### Data Cleaning

```bash
python src/clean.py
```

### Exploratory Data Analysis

```bash
python src/eda.py
```

---

## Current Status

### Completed

* Project Setup
* Git & GitHub Configuration
* Data Ingestion
* Data Quality Assessment
* Data Cleaning
* Data Quality Reporting
* Exploratory Data Analysis
* Data Visualization



Polyhouse Mushroom Yield Analysis Project


## Feature Engineering

### Input Features

| Feature | Description |
|----------|-------------|
| temperature_c | Polyhouse temperature in °C |
| humidity_pct | Relative humidity (%) |
| co2_ppm | Carbon dioxide concentration (ppm) |
| temp_humid_interaction | Interaction feature combining temperature and humidity |

### Engineered Feature Formula

temp_humid_interaction = temperature_c × humidity_pct / 100

### Target Variable

yield_kg = Mushroom yield in kilograms

### Scaling

Features were normalized using MinMaxScaler to transform values into the range [0, 1].

## Train/Test Split

The dataset was first sorted chronologically using the `timestamp` column to preserve temporal order and prevent data leakage.

An 80/20 chronological split was applied:

### Training Set

* Rows: 292 (80%)
* Date Range: 2024-01-01 to 2024-10-18

### Test Set

* Rows: 73 (20%)
* Date Range: 2024-10-19 to 2024-12-30

### Data Leakage Prevention

To ensure realistic forecasting performance, all training observations occur before the test period. A validation check confirmed that the earliest test timestamp is later than the latest training timestamp.

### Feature Scaling

A `MinMaxScaler` was fitted using only the training data. The fitted scaler was then used to transform both training and test features, preventing leakage of future information from the test set.


