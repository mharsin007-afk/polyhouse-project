\# GridSearchCV Hyperparameter Tuning



\## Objective



The objective of this task was to improve the Random Forest model by tuning key hyperparameters using GridSearchCV while preserving temporal order through TimeSeriesSplit cross-validation.



\## Parameter Grid



The following parameter grid was evaluated:



```python

param\_grid = {

&#x20;   "n\_estimators": \[50, 100, 200],

&#x20;   "max\_depth": \[None, 8, 16],

&#x20;   "min\_samples\_leaf": \[1, 3, 5]

}

```



\### Rationale



\* \*\*n\_estimators\*\*: Controls the number of trees in the forest. More trees can improve stability but increase computation time.

\* \*\*max\_depth\*\*: Limits tree growth and helps control overfitting.

\* \*\*min\_samples\_leaf\*\*: Prevents trees from creating overly specific leaf nodes, improving generalization.



\## Cross-Validation Strategy



GridSearchCV was performed using:



\* TimeSeriesSplit with 3 folds

\* Training data only (`train.csv`)

\* Scoring metric: Mean Absolute Error (MAE)



This approach prevents data leakage by ensuring future observations are never used to predict past observations.



\## Best Hyperparameters



```json

{

&#x20; "max\_depth": 8,

&#x20; "min\_samples\_leaf": 5,

&#x20; "n\_estimators": 100

}

```



\### Best Cross-Validation Score



| Metric | Value |

| ------ | ----- |

| CV MAE | 0.465 |



\## Test Set Evaluation



After selecting the best estimator, the model was evaluated once on the held-out test set.



| Metric | Value |

| ------ | ----- |

| MAE    | 0.445 |

| RMSE   | 0.562 |

| R²     | 0.369 |



\## Comparison with Previous Models



| Model                 | MAE       | RMSE      | R²        |

| --------------------- | --------- | --------- | --------- |

| Linear Regression     | 0.470     | 0.592     | 0.289     |

| Default Random Forest | 0.449     | 0.580     | 0.328     |

| Tuned Random Forest   | \*\*0.445\*\* | \*\*0.562\*\* | \*\*0.369\*\* |



The tuned Random Forest achieved the best overall performance, improving prediction accuracy and model fit compared to both the baseline Linear Regression and the default Random Forest.



\## Runtime



| Item                | Value        |

| ------------------- | ------------ |

| Grid Search Runtime | 8.97 seconds |



The runtime was reasonable for a laptop environment and allowed efficient experimentation with multiple hyperparameter combinations.



\## Artifacts Saved



\* `models/random\_forest\_tuned.joblib`

\* `models/rf\_best\_params.json`

\* `reports/grid\_search\_cv\_results.csv`



\## Conclusion



GridSearchCV successfully identified a better-performing Random Forest configuration. Restricting tree depth and increasing the minimum samples per leaf reduced overfitting and improved generalization. The tuned Random Forest is the strongest model developed so far and will be used as the candidate production model for subsequent evaluation and comparison tasks.



