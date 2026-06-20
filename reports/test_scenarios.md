\# Prediction Validation Scenarios



| Scenario | Temp (°C) | Humidity (%) | CO₂ (ppm) | CLI Prediction (kg) | App Prediction (kg) | Match |

|-----------|-----------|---------------|------------|---------------------|---------------------|-------|

| Optimal | 22 | 88 | 920 | 17.00 | 17.00 | ✅ |

| Dry spell | 22 | 60 | 920 | 16.94 | 16.94 | ✅ |

| Heat spike | 32 | 88 | 920 | 18.16 | 18.16 | ✅ |

| Extreme CO₂ | 22 | 88 | 1800 | 16.76 | 16.76 | ✅ |

| Multiple stressors | 32 | 60 | 1800 | 18.05 | 18.05 | ✅ |



\## Notes



\- Predictions from the Streamlit app and `predict.py` CLI matched exactly for all sampled scenarios.

\- Lower humidity slightly reduced predicted yield (17.00 → 16.94 kg).

\- Higher CO₂ reduced predicted yield (17.00 → 16.76 kg).

\- The model predicts higher yield at 32°C, indicating temperature is a strong positive predictor in the training data.

\- The combined stressor scenario (32°C, 60% humidity, 1800 ppm CO₂) still produced a high prediction because the positive effect of temperature outweighed the negative effects of humidity and CO₂ in the learned model.

\- Scenario outcomes reflect patterns learned from the training dataset and may differ from expected biological behavior.

