\# Mushroom Yield Forecast



\## Zelbytes Agritech Capstone



\*\*Presenter:\*\* Muhammad Harsin



\*\*Repository:\*\* https://github.com/mharsin007-afk/polyhouse-project



\---



\# Slide 1: Project Overview



\## Objective



Develop an end-to-end machine learning system to predict daily oyster mushroom yield using polyhouse environmental sensor data.



\## Business Goal



Enable data-driven harvest planning and improve operational efficiency.



\---



\# Slide 2: Agritech Problem



Mushroom cultivation depends heavily on environmental conditions.



Key challenges include:



\* Uncertain daily yield estimates

\* Inefficient harvest planning

\* Inventory shortages or overproduction

\* Manual decision-making



\## Target Variable



\* Daily mushroom yield (kg)



\## Input Features



\* Temperature (℃)

\* Humidity (%)

\* CO₂ concentration (ppm)



\---



\# Slide 3: Dataset and Pipeline



\## Dataset



\* Observation period: January 2024 to December 2024

\* Cleaned records: 360



\## Pipeline



Raw Data → Ingestion → Cleaning → EDA → Feature Engineering → Model Training → Deployment → Monitoring



\## Tools



\* Python

\* Pandas

\* Scikit-learn

\* Streamlit

\* Joblib

\* Git and GitHub



\---



\# Slide 4: Data Cleaning and EDA



\## Data Quality Steps



\* Removed duplicates

\* Handled missing values

\* Filtered invalid sensor ranges



\### Valid Ranges



\* Temperature: 10–35 ℃

\* Humidity: 50–100 %

\* CO₂: 400–2000 ppm



\## Key Findings



\* Temperature positively correlated with yield (r = 0.524)

\* Humidity weakly correlated with yield (r = 0.242)

\* CO₂ negatively correlated with yield (r = -0.260)



Include screenshots:



\* Correlation heatmap

\* Scatter plots



\---



\# Slide 5: Modeling Approach



\## Validation Strategy



Chronological train-test split:



\* Train: January–October 2024

\* Test: October–December 2024



\## Why Temporal Splitting?



Prevents data leakage by ensuring future observations are not used during training.



\## Models Evaluated



\* Linear Regression

\* Random Forest

\* Tuned Random Forest



\---



\# Slide 6: Model Results



| Model               | Test MAE (kg) | Test RMSE (kg) | Test R²   |

| ------------------- | ------------- | -------------- | --------- |

| Linear Regression   | 0.470         | 0.592          | 0.289     |

| Random Forest       | 0.449         | 0.580          | 0.328     |

| Tuned Random Forest | \*\*0.445\*\*     | \*\*0.562\*\*      | \*\*0.369\*\* |



\## Champion Model



Tuned Random Forest



\### Feature Importance



\* Temperature: 57.0 %

\* Humidity: 23.6 %

\* CO₂: 19.4 %



\---



\# Slide 7: Deployment and Monitoring



\## Deployment



Streamlit application with real-time predictions.



User inputs:



\* Temperature (℃)

\* Humidity (%)

\* CO₂ concentration (ppm)



Output:



\* Predicted mushroom yield (kg)



\## Monitoring



Logged fields:



\* timestamp\_utc

\* temp\_c

\* humidity\_pct

\* co2\_ppm

\* predicted\_kg



\## Retraining Trigger



Weekly MAE > 0.534 kg for two consecutive weeks.



\---



\# Slide 8: Live Demo



\## Demonstration Flow



1\. Open Streamlit application

2\. Change sensor values

3\. Generate prediction

4\. Verify prediction logs



\### Backup Plan



Include screenshots of:



\* Streamlit home screen

\* Example prediction

\* Prediction log file



\## Deployment URL



\[Add your Streamlit URL here]



\---



\# Slide 9: Lessons Learned



\## Technical Skills Developed



\* Data cleaning and quality assessment

\* Machine learning model evaluation

\* Deployment and monitoring workflows



\## Key Concepts Learned



\* Data leakage prevention

\* Temporal validation strategies

\* Model monitoring and drift detection



\---



\# Slide 10: Limitations and Future Work



\## Limitations



\* One year of data

\* Limited environmental variables

\* Potential sensor calibration errors



\## Future Improvements



\* Add seasonal features

\* Automate retraining

\* Build monitoring dashboard

\* Evaluate XGBoost and LightGBM



\---



\# Slide 11: Reflection



\## Top 3 Skills Learned



1\. Building end-to-end machine learning pipelines

2\. Deploying models with Streamlit

3\. Monitoring model performance after deployment



\## Areas for Growth



1\. Advanced feature engineering

2\. MLOps and automated deployment pipelines



\---



\# Slide 12: Thank You



Questions and Discussion



Repository: https://github.com/mharsin007-afk/polyhouse-project



Technical Report: reports/final\_report.md



Deployment URL: \[Add your Streamlit URL here]



