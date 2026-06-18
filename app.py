
import numpy as np
import pandas as pd
import streamlit as st

from src.predict import load_artifacts, predict_yield

# -------------------------------------------------------------------
# Page configuration
# -------------------------------------------------------------------

st.set_page_config(
    page_title="Zelbytes Agritech | Polyhouse Yield Predictor",
    page_icon="🍄",
    layout="centered"
)

# -------------------------------------------------------------------
# Custom styling
# -------------------------------------------------------------------

st.markdown(
    """
    <style>
        .main-header {
            color: #2E8B57;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------------
# Cache model artifacts
# -------------------------------------------------------------------

@st.cache_resource
def get_artifacts():
    return load_artifacts()


model, scaler, feature_cols = get_artifacts()

# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------

st.markdown(
    "<h1 class='main-header'>🍄 Zelbytes Agritech</h1>",
    unsafe_allow_html=True
)

st.subheader("Polyhouse Yield Forecast")

st.markdown(
    """
    Estimate daily mushroom yield from environmental sensor readings.

    **Sensor units**

    - Temperature: degrees Celsius (°C)
    - Relative Humidity: percent (%)
    - CO₂ concentration: parts per million (ppm)
    """
)

st.markdown(
    "[View methodology documentation](README.md)"
)

# -------------------------------------------------------------------
# Sidebar inputs
# -------------------------------------------------------------------

with st.sidebar:
    st.header("Sensor Inputs")

    temp = st.slider(
        "Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.0,
        step=0.1
    )

    humid = st.slider(
        "Humidity (%)",
        min_value=50.0,
        max_value=100.0,
        value=88.0,
        step=0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        min_value=400,
        max_value=2000,
        value=900,
        step=10
    )

# -------------------------------------------------------------------
# Warnings
# -------------------------------------------------------------------

if temp < 15 or temp > 30:
    st.warning(
        "Temperature is outside the typical training range (15–30°C)."
    )

if humid < 70 or humid > 95:
    st.warning(
        "Humidity is outside the typical training range (70–95%)."
    )

if co2 < 500 or co2 > 1500:
    st.warning(
        "CO₂ is outside the typical training range (500–1500 ppm)."
    )

# -------------------------------------------------------------------
# Prediction
# -------------------------------------------------------------------

if st.button("Predict Yield", use_container_width=True):

    prediction = predict_yield(
        model,
        scaler,
        feature_cols,
        temp,
        humid,
        co2
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Estimated Daily Yield",
            value=f"{prediction:.2f} kg"
        )

    with col2:
        st.metric(
            label="Humidity",
            value=f"{humid:.1f}%"
        )

    st.divider()

    st.subheader("What-if Analysis: Humidity Sweep")

    humid_range = np.linspace(70, 98, 29)

    preds = [
        predict_yield(
            model,
            scaler,
            feature_cols,
            temp,
            h,
            co2
        )
        for h in humid_range
    ]

    chart_df = pd.DataFrame(
        {
            "Humidity (%)": humid_range,
            "Predicted Yield (kg)": preds
        }
    )

    st.line_chart(
        chart_df,
        x="Humidity (%)",
        y="Predicted Yield (kg)",
        use_container_width=True
    )

# -------------------------------------------------------------------
# Model metadata
# -------------------------------------------------------------------

with st.expander("Model Information"):

    st.markdown(
        """
        - **Model version:** v1.0
        - **Algorithm:** Tuned Random Forest Regressor
        - **Training period:** January–December 2024
        - **Test MAE:** 0.445 kg/day
        - **Test RMSE:** 0.562 kg/day
        - **Test R²:** 0.369
        - **Last trained:** 18 June 2026
        """
    )

st.caption(
    "Zelbytes Agritech • Decision support for controlled-environment mushroom cultivation"
)

