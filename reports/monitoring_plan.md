\# Model Monitoring and Iteration Plan



\## Inference Logging



The deployed mushroom yield prediction system records each inference request for monitoring and future model improvement.



The following fields are logged to `logs/predictions.csv`:



| Field           | Description                                       |

| --------------- | ------------------------------------------------- |

| `timestamp\_utc` | UTC timestamp when the prediction was generated   |

| `temp\_c`        | Polyhouse temperature in degrees Celsius          |

| `humidity\_pct`  | Relative humidity percentage                      |

| `co2\_ppm`       | Carbon dioxide concentration in parts per million |

| `predicted\_kg`  | Predicted mushroom yield in kilograms             |



Only sensor measurements and model outputs are stored. No personally identifiable information (PII) or farmer-specific data is collected.



\## Monitoring Metrics



The following metrics will be monitored after deployment:



\* Daily prediction volume

\* Distribution of temperature, humidity, and CO₂ measurements

\* Range and distribution of predicted yields

\* Weekly Mean Absolute Error (MAE) using newly collected harvest data

\* Percentage of missing or invalid sensor readings



Monitoring these metrics helps identify model degradation and operational issues early.



\## Data Drift Scenarios



Potential causes of data drift include:



\* Sensor firmware updates affecting humidity measurements

\* Sensor recalibration or replacement

\* Seasonal changes in environmental conditions

\* Changes in mushroom cultivation practices

\* Long-term sensor degradation or hardware faults



These factors may cause incoming data to differ from the original training dataset and reduce prediction accuracy.



\## Alert Thresholds



Alerts should be triggered when:



\* Predicted yield exceeds the historical maximum yield by more than 10%

\* Missing or invalid sensor readings exceed 5% of daily records

\* Significant changes are detected in input feature distributions

\* Weekly MAE increases by more than 20% above the baseline test MAE



\## Retraining Strategy



The baseline test MAE of the deployed Random Forest model is 0.445 kg.



The model should be retrained when:



\* Weekly MAE exceeds 0.534 kg for two consecutive weeks

\* Significant feature drift is detected

\* New sensor hardware or firmware is deployed

\* At least one month of new harvest data is available



Retraining will incorporate the latest sensor and harvest records to maintain prediction performance.



\## Business Impact



Accurate yield predictions improve harvest planning, inventory management, and resource allocation. Monitoring reduces the risk of inaccurate forecasts that may lead to wasted harvest trips, inefficient labour allocation, stock shortages, or excess inventory.



\## Iteration Roadmap



Future improvements for the system include:



1\. Add time-based features such as season, month, and rolling averages.

2\. Automate weekly retraining using newly collected harvest data.

3\. Build a monitoring dashboard for model performance and data drift.

4\. Implement anomaly alerts for unusual predictions.

5\. Evaluate advanced models such as XGBoost and LightGBM.



