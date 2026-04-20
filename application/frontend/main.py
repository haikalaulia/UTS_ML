import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Agro ML Predictor", layout="centered")

st.title("🌱 Agro-Environmental Suitability Predictor")

st.write("Masukkan kondisi lingkungan dan tanah untuk memprediksi apakah tanaman dapat tumbuh.")

# =========================
# Input Form
# =========================
with st.form("prediction_form"):

    st.subheader("Soil Properties")
    bulk_density = st.number_input("Bulk Density", 0.0, 3.0, 1.2)
    organic_matter = st.number_input("Organic Matter (%)", 0.0, 100.0, 5.0)
    cec = st.number_input("Cation Exchange Capacity", 0.0, 100.0, 10.0)
    salinity = st.number_input("Salinity", 0.0, 50.0, 1.0)
    buffering = st.number_input("Buffering Capacity", 0.0, 50.0, 5.0)

    st.subheader("Environmental Conditions")
    soil_moisture = st.number_input("Soil Moisture", 0.0, 100.0, 30.0)
    soil_temp = st.number_input("Soil Temperature (°C)", 0.0, 60.0, 25.0)
    air_temp = st.number_input("Air Temperature (°C)", 0.0, 60.0, 28.0)
    light = st.number_input("Light Intensity", 0.0, 2000.0, 800.0)
    ph = st.number_input("pH", 0.0, 14.0, 6.5)

    st.subheader("Derived Features")
    moisture_regime = st.selectbox("Moisture Regime", [0, 1, 2])
    thermal_regime = st.selectbox("Thermal Regime", [0, 1, 2])
    nutrient_balance = st.number_input("Nutrient Balance", -100.0, 100.0, 0.0)

    submit = st.form_submit_button("Predict")


# =========================
# Handle Prediction
# =========================
if submit:
    payload = {
        "bulk_density": bulk_density,
        "organic_matter": organic_matter,
        "cation_exchange_capacity": cec,
        "salinity": salinity,
        "buffering_capacity": buffering,
        "soil_moisture": soil_moisture,
        "soil_temperature": soil_temp,
        "air_temperature": air_temp,
        "light_intensity": light,
        "ph": ph,
        "moisture_regime": moisture_regime,
        "thermal_regime": thermal_regime,
        "nutrient_balance": nutrient_balance
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            if "prediction" in result:
                st.success(f"Hasil Prediksi: {result['interpretation']}")
            else:
                st.error(result.get("error", "Unknown error"))
        else:
            st.error("Gagal menghubungi backend")

    except Exception as e:
        st.error(f"Error: {e}")
