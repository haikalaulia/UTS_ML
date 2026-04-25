import streamlit as st

# Konfigurasi endpoint API (mengambil dari secrets, fallback ke localhost jika tidak tersedia)
try:
    API_BASE_URL = st.secrets["API_BASE_URL"]
except Exception:
    API_BASE_URL = "http://127.0.0.1:8000"

PREDICT_URL = f"{API_BASE_URL}/predict"  # Endpoint untuk melakukan prediksi
HEALTH_URL  = f"{API_BASE_URL}/health"   # Endpoint untuk cek status backend

# Konfigurasi halaman aplikasi (judul, ikon, dan versi aplikasi)
PAGE_TITLE  = "AgroSense · ML Dashboard"
PAGE_ICON   = "🌿"
APP_VERSION = "v2.0"

# Informasi model machine learning yang digunakan dalam sistem
MODEL_NAME      = "Random Forest"
MODEL_TUNING    = "GridSearchCV"
MODEL_TASK      = "Binary Classification"
MODEL_TARGET    = "failure_flag"