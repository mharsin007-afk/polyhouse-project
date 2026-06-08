\# Polyhouse Sensor Project



\## Project Goal



The goal of this project is to monitor polyhouse environmental conditions for mushroom cultivation and analyze how factors such as temperature, humidity, and CO₂ concentration affect mushroom yield.



\## Dataset



The dataset contains sensor readings collected from a mushroom polyhouse environment.



\### Features



\* Timestamp

\* Temperature (°C)

\* Humidity (%)

\* CO₂ Concentration (ppm)

\* Yield (kg)



\## Project Structure



```text

polyhouse-project/

├── data/

│   ├── raw/

│   └── interim/

├── reports/

│   ├── figures/

│   ├── data\_quality.md

│   └── eda\_notes.md

├── src/

│   ├── ingest.py

│   ├── clean.py

│   └── eda.py

├── models/

└── README.md

```



\## Project Pipeline



```text

Raw CSV Data

&#x20;     ↓

Data Ingestion

&#x20;     ↓

Data Quality Assessment

&#x20;     ↓

Data Cleaning

&#x20;     ↓

Cleaned Dataset

&#x20;     ↓

Exploratory Data Analysis

&#x20;     ↓

Visualizations \& Insights

```



\---



\## Task 1: Data Ingestion



\### Objective



Load raw sensor data and prepare it for processing.



\### Work Completed



\* Loaded CSV data using Pandas.

\* Parsed timestamp values.

\* Verified data types.

\* Stored processed data in Parquet format.



\### Output



\* `src/ingest.py`

\* `data/interim/01\_loaded.parquet`



\---



\## Task 2: Data Quality Assessment \& Data Cleaning



\### Objective



Identify missing values, invalid sensor readings, and data quality issues before analysis.



\### Data Quality Checks



The following checks were performed:



\* Missing value analysis

\* Data type verification

\* Range validation

\* Summary statistics generation

\* Detection of invalid observations



\### Cleaning Rules



| Column        | Valid Range          |

| ------------- | -------------------- |

| temperature\_c | 10–35 °C             |

| humidity\_pct  | 50–100 %             |

| co2\_ppm       | ≥ 400 ppm            |

| yield\_kg      | Positive values only |



\### Work Completed



\* Audited missing values.

\* Removed invalid observations.

\* Applied agritech-based validation rules.

\* Generated a cleaned dataset.

\* Documented null counts before and after cleaning.



\### Outputs



\* `src/clean.py`

\* `reports/data\_quality.md`

\* `data/interim/02\_cleaned.parquet`



\---



\## Task 3: Exploratory Data Analysis (EDA)



\### Objective



Explore relationships between environmental variables and mushroom yield.



\### Visualizations Generated



\#### Correlation Heatmap



Analyzed correlations among:



\* Temperature

\* Humidity

\* CO₂

\* Yield



\#### Scatter Plots



Generated scatter plots for:



\* Humidity vs Yield

\* Temperature vs Yield

\* CO₂ vs Yield



\### Key Findings



\* Temperature showed the strongest positive correlation with yield.

\* Humidity showed a moderate positive relationship with yield.

\* CO₂ concentration showed a weak negative relationship with yield.



\### Outputs



\* `src/eda.py`

\* `reports/eda\_notes.md`

\* `reports/figures/corr\_heatmap.png`

\* `reports/figures/scatter\_yield.png`



\---



\## Technologies Used



\* Python

\* Pandas

\* Matplotlib

\* Parquet

\* Git

\* GitHub



\---



\## How to Run



\### Data Ingestion



```bash

python src/ingest.py

```



\### Data Cleaning



```bash

python src/clean.py

```



\### Exploratory Data Analysis



```bash

python src/eda.py

```



\---



\## Current Status



\### Completed



\* Project Setup

\* Git \& GitHub Configuration

\* Data Ingestion

\* Data Quality Assessment

\* Data Cleaning

\* Data Quality Reporting

\* Exploratory Data Analysis

\* Data Visualization



\### Upcoming



\* Feature Engineering

\* Machine Learning Models

\* Model Evaluation

\* Yield Prediction

\* Streamlit Dashboard

\* Deployment



\---



\## Author





Polyhouse Mushroom Yield Analysis Project



