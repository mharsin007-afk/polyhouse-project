\# Reproducibility Note



\## Saved Artifacts



The deployment pipeline uses the following saved artifacts:



\* `models/random\_forest\_tuned.joblib`

\* `models/minmax\_scaler\_train.joblib`

\* `models/feature\_cols.json`



\## Feature Order



The model expects features in the following order:



1\. temperature\_c

2\. humidity\_pct

3\. co2\_ppm



This order must remain unchanged during inference.



\## Random Seed



The project uses:



random\_state = 42



for Random Forest training and hyperparameter tuning to ensure reproducibility.



\## Environment



The project was developed using:



\* Python 3.13

\* pandas

\* numpy

\* scikit-learn

\* matplotlib

\* joblib



Exact package versions are recorded in `requirements.txt`.



\## Running Inference



Command-line test:



python src/predict.py



Example Python usage:



from src.predict import predict\_yield



prediction = predict\_yield(

temperature\_c=22,

humidity\_pct=88,

co2\_ppm=920

)



print(prediction)



The function returns the predicted mushroom yield in kilograms.



