\# Mushroom Yield Forecast Using Polyhouse Sensor Data



\## Executive Summary



This project developed a machine learning system to predict daily oyster mushroom yield in a controlled polyhouse environment using environmental sensor data. The objective was to estimate yield from temperature (℃), humidity (%), and carbon dioxide concentration (ppm) to support harvest planning and resource allocation.



Three regression models were evaluated: Linear Regression, Random Forest, and Tuned Random Forest. The tuned Random Forest model achieved the best performance with a test Mean Absolute Error (MAE) of \*\*0.445 kg\*\*, Root Mean Squared Error (RMSE) of \*\*0.562 kg\*\*, and coefficient of determination (R²) of \*\*0.369\*\*.



The selected model was deployed through a Streamlit application and enhanced with structured prediction logging to support monitoring, drift detection, and future retraining.



\---



\## 1. Problem Statement and Agritech Context



Mushroom cultivation requires precise environmental control to achieve consistent yields. Temperature, humidity, and carbon dioxide concentration significantly influence mushroom growth within polyhouse environments.



Traditional yield estimation methods rely on manual observations and grower experience, which may lead to inaccurate harvest planning, inefficient labour allocation, inventory imbalances, and increased operational costs.



The objective of this project was to build a data-driven system capable of predicting daily oyster mushroom yield from sensor measurements collected within a polyhouse.



\### Business Objectives



\* Improve harvest planning accuracy

\* Reduce inventory shortages and overproduction

\* Support data-driven cultivation decisions

\* Enable scalable monitoring of multiple polyhouses



\---



\## 2. Data Description



The dataset consists of sensor measurements collected from a mushroom polyhouse during 2024.



\### Variables



| Feature       | Unit     | Description                  |

| ------------- | -------- | ---------------------------- |

| timestamp     | DateTime | Sensor observation timestamp |

| temperature\_c | ℃        | Polyhouse air temperature    |

| humidity\_pct  | %        | Relative humidity            |

| co2\_ppm       | ppm      | Carbon dioxide concentration |

| yield\_kg      | kg       | Daily mushroom yield         |



\### Dataset Summary



\* Observation period: January 2024 to December 2024

\* Total cleaned records: 360

\* Target variable: `yield\_kg`



\---



\## 3. Data Cleaning and Quality Assessment



Data quality checks were implemented to ensure reliable model training.



\### Cleaning Steps



\* Removed duplicate records

\* Forward-filled missing sensor values with a maximum limit of two consecutive observations

\* Removed rows with missing yield values

\* Filtered unrealistic sensor readings using domain constraints



\### Valid Sensor Ranges



| Feature       | Accepted Range |

| ------------- | -------------- |

| temperature\_c | 10–35 ℃        |

| humidity\_pct  | 50–100 %       |

| co2\_ppm       | 400–2000 ppm   |



The cleaned dataset was saved as:



```text

data/interim/02\_cleaned.parquet

```



\---



\## 4. Exploratory Data Analysis



Exploratory analysis was conducted to understand relationships between environmental variables and mushroom yield.



\### Correlation Findings



\* Temperature exhibited a moderate positive relationship with yield (r = 0.524)

\* Humidity exhibited a weak positive relationship with yield (r = 0.242)

\* CO₂ concentration exhibited a weak negative relationship with yield (r = -0.260)



\### Key Insights



\* Higher temperatures within the acceptable cultivation range were associated with increased yields.

\* Extremely high CO₂ concentrations tended to reduce yield.

\* Humidity influenced yield but had lower predictive power than temperature.



\### Figures



\#### Correlation Heatmap



```markdown

!\[Correlation Heatmap](figures/corr\_heatmap.png)

```



\#### Yield Relationship Scatter Plots



```markdown

!\[Yield Relationships](figures/scatter\_yield.png)

```



\---



\## 5. Feature Engineering and Validation Strategy



A feature interaction term was initially evaluated:



\* `temp\_humid\_interaction = temperature\_c × humidity\_pct / 100`



Final model training used the following features:



\* temperature\_c

\* humidity\_pct

\* co2\_ppm



\### Temporal Train-Test Split



The dataset was sorted chronologically before splitting.



\* Training period: 2024-01-01 to 2024-10-18

\* Testing period: 2024-10-19 to 2024-12-30



\### Why Temporal Splitting Matters



Randomly shuffling time-series data can introduce data leakage by allowing information from future observations to influence model training.



Using a chronological split better simulates real-world deployment because future yield predictions are generated using only historical information.



\### Feature Scaling



A MinMaxScaler was fitted exclusively on training data to avoid data leakage.



\---



\## 6. Models Evaluated



Three regression models were evaluated.



\### Linear Regression



Linear Regression provides a simple and interpretable baseline model that assumes a linear relationship between environmental conditions and yield.



\### Random Forest



Random Forest is an ensemble learning method that combines multiple decision trees to capture nonlinear relationships.



\### Tuned Random Forest



GridSearchCV and TimeSeriesSplit cross-validation were used to optimise hyperparameters.



Best hyperparameters:



\* n\_estimators: 100

\* max\_depth: 8

\* min\_samples\_leaf: 5



\---



\## 7. Results and Champion Model Selection



\### Evaluation Metrics



Mean Absolute Error (MAE) measures the average prediction error in kilograms.



For example, an MAE of 0.445 kg indicates that predictions differ from actual yield by approximately 445 grams on average.



\### Model Comparison



| Model               | CV MAE (kg) | Test MAE (kg) | Test RMSE (kg) | Test R²   |

| ------------------- | ----------- | ------------- | -------------- | --------- |

| Linear Regression   | 0.440       | 0.470         | 0.592          | 0.289     |

| Random Forest       | 0.474       | 0.449         | 0.580          | 0.328     |

| Tuned Random Forest | 0.465       | \*\*0.445\*\*     | \*\*0.562\*\*      | \*\*0.369\*\* |



\### Champion Model



The Tuned Random Forest model was selected because it achieved the lowest test MAE and RMSE while maintaining the highest R² score.



Feature importance analysis showed:



\* Temperature: 57.0%

\* Humidity: 23.6%

\* CO₂ concentration: 19.4%



\---



\## 8. Deployment



The selected model was deployed using Streamlit.



The application enables users to enter:



\* Temperature (℃)

\* Humidity (%)

\* CO₂ concentration (ppm)



The application returns an estimated mushroom yield in kilograms.



\### Deployment Components



\* `app.py`

\* `src/predict.py`

\* `models/random\_forest\_tuned.joblib`

\* `models/minmax\_scaler\_train.joblib`

\* `models/feature\_cols.json`



\---



\## 9. Monitoring and Operations



Prediction logging was implemented to support model monitoring.



Each prediction records:



\* timestamp\_utc

\* temp\_c

\* humidity\_pct

\* co2\_ppm

\* predicted\_kg



Logs are stored in:



```text

logs/predictions.csv

```



\### Monitoring Metrics



\* Prediction volume

\* Input feature distributions

\* Prediction range checks

\* Weekly MAE using new harvest data



\### Retraining Triggers



The model should be retrained when:



\* Weekly MAE exceeds 0.534 kg for two consecutive weeks

\* Sensor firmware changes are deployed

\* Significant feature drift is detected

\* One month of new harvest data becomes available



\---



\## 10. Limitations



Several limitations should be considered when interpreting the results.



\* The dataset contains only one year of observations.

\* External factors such as substrate quality, irrigation schedules, and disease incidence were not included.

\* The model was trained using a relatively small dataset.

\* Sensor calibration errors may affect prediction quality.

\* Environmental conditions may vary across different polyhouse locations.



\---



\## 11. Future Work



Potential improvements include:



1\. Add seasonal and time-based features.

2\. Incorporate additional sensors such as light intensity and substrate moisture.

3\. Automate weekly retraining workflows.

4\. Implement real-time drift detection dashboards.

5\. Evaluate advanced ensemble models such as XGBoost and LightGBM.

6\. Collect multi-year data to improve generalisation.



\---



\## Appendix A: Reproducibility



\### Clone Repository



```bash

git clone https://github.com/mharsin007-afk/polyhouse-project.git

cd polyhouse-project

```



\### Create Virtual Environment



```bash

python -m venv .venv

```



\### Activate Environment



\#### Windows



```bash

.venv\\Scripts\\activate

```



\#### Linux or macOS



```bash

source .venv/bin/activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Run Data Pipeline



```bash

python src/ingest.py

python src/clean.py

python src/eda.py

python src/features.py

python src/split\_scale.py

```



\### Train Models



```bash

python src/train\_linear.py

python src/train\_random\_forest.py

python src/grid\_search\_rf.py

python src/model\_comparison.py

```



\### Launch Application



```bash

streamlit run app.py

```



