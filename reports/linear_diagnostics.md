\# Linear Regression Diagnostics



\## Diagnostic Figures



\* reports/figures/residuals\_vs\_predicted\_linear.png

\* reports/figures/residuals\_vs\_humidity\_linear.png



\## Findings



\### Residuals vs Predicted Yield



Residuals are generally centered around zero and appear randomly distributed across predicted yield values. No strong curvature pattern is visible, suggesting that the linear model captures the primary relationships in the data. Error variance remains relatively consistent across the prediction range, indicating no severe heteroscedasticity. One moderate outlier is present but does not dominate model performance.



\### Residuals vs Humidity



Residuals show no clear trend with humidity. Errors are distributed on both sides of zero throughout the humidity range, indicating that humidity is reasonably represented within the model. A few larger residuals occur at mid-range humidity values but do not form a systematic pattern.



\### Train vs Test Comparison



Training and testing residual standard deviations are very similar (0.520 vs 0.525), suggesting that the model generalizes consistently and shows little evidence of overfitting.



\## Recommendation



Linear Regression provides a reasonable baseline model for mushroom yield prediction. Diagnostic plots do not reveal major violations of model assumptions. However, the test R² score of 0.427 indicates that additional variability remains unexplained. Future work should evaluate additional features and nonlinear models such as Random Forest Regression to determine whether predictive performance can be improved.



