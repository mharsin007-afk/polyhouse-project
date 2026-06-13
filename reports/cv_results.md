\# Cross-Validation \& Overfitting Analysis



TimeSeriesSplit with three folds was used to evaluate model stability while preserving temporal order. Cross-validation was performed only on the training dataset to avoid data leakage.



\## Linear Regression



Fold 1 MAE: 0.462



Fold 2 MAE: 0.451



Fold 3 MAE: 0.407



Mean CV MAE: 0.440



Standard Deviation: 0.024



\## Random Forest



Fold 1 MAE: 0.514



Fold 2 MAE: 0.469



Fold 3 MAE: 0.438



Mean CV MAE: 0.474



Standard Deviation: 0.031



\## Overfitting Analysis



Linear Regression showed minimal overfitting with Train MAE = 0.424 and Test MAE = 0.470.



Random Forest showed moderate overfitting with Train MAE = 0.166 and Test MAE = 0.449, indicating stronger fitting to the training data than unseen data.



\## Interpretation



Variance across folds was low for both models, suggesting stable performance over time. Cross-validation results indicate that Linear Regression generalized slightly better across folds, while Random Forest achieved slightly better performance on the hold-out test set. These results provide a foundation for future hyperparameter tuning using GridSearch.



