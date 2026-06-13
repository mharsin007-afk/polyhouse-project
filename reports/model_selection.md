\# Model Comparison and Champion Selection



\## Model Comparison



| Model               | CV MAE | Test MAE |  RMSE |    R² | Interpretability |

| ------------------- | -----: | -------: | ----: | ----: | ---------------- |

| Linear Regression   |  0.440 |    0.470 | 0.592 | 0.289 | High             |

| Random Forest       |  0.474 |    0.449 | 0.580 | 0.328 | Medium           |

| Tuned Random Forest |  0.465 |    0.445 | 0.562 | 0.369 | Medium-Low       |



\## Champion Model



The Tuned Random Forest was selected as the champion model.



It achieved the lowest Test MAE (0.445), lowest RMSE (0.562), and highest R² (0.369) among all evaluated models. Although Linear Regression offers greater interpretability, the tuned Random Forest consistently delivered more accurate yield predictions.



For agritech decision-making, prediction accuracy is important because overestimating yield can create supply commitments that cannot be fulfilled, while underestimating yield can lead to inefficient harvest planning and labor allocation. The tuned Random Forest provides the best balance between predictive performance and operational usefulness.



\## Predicted vs Actual Analysis



A predicted-versus-actual scatter plot was generated for the champion model and saved as:



`reports/figures/pred\_vs\_actual.png`



Most predictions cluster near the ideal diagonal line, indicating that the model captures a substantial portion of the relationship between environmental conditions and mushroom yield.



\## Limitations



\* The model was trained on historical sensor readings and may perform poorly when temperature, humidity, or CO₂ values fall outside the ranges observed during training.

\* Seasonal effects and environmental conditions not represented in the dataset may reduce prediction accuracy.

\* The dataset covers a limited period and may not capture all production scenarios.

\* The model should be used as a decision-support tool rather than a replacement for grower expertise and operational judgment.

\* Additional years of data would likely improve robustness and generalization.



\## Deployment Recommendation



The Tuned Random Forest is recommended as the deployment candidate because it achieved the strongest overall performance across evaluation metrics while maintaining reasonable training time and acceptable model complexity.



\### Final Performance Summary



| Model                   |  Test MAE |      RMSE |        R² |

| ----------------------- | --------: | --------: | --------: |

| Linear Regression       |     0.470 |     0.592 |     0.289 |

| Random Forest           |     0.449 |     0.580 |     0.328 |

| \*\*Tuned Random Forest\*\* | \*\*0.445\*\* | \*\*0.562\*\* | \*\*0.369\*\* |



The tuned Random Forest will be carried forward for model serialization and Streamlit deployment.



