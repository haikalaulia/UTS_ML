from __future__ import annotations

import os
from pathlib import Path

# Menentukan path dasar direktori file saat ini dan root project
BASE_DIR = Path(__file__).resolve().parent[2]
PROJECT_ROOT = BASE_DIR.parent

# Menentukan path default model machine learning (file .pkl)
DEFAULT_MODEL_PATH = PROJECT_ROOT / "model" / "random_forest_tuned_pipeline.pkl"

# Mengambil path model dari environment variable jika ada, jika tidak gunakan default path
MODEL_PATH = Path(os.getenv("MODEL_PATH", str(DEFAULT_MODEL_PATH)))

# Konfigurasi metadata API (judul dan versi) yang dapat diatur melalui environment variable
API_TITLE = os.getenv("API_TITLE", "Agro Environmental Failure Prediction API")
API_VERSION = os.getenv("API_VERSION", "1.0.0")

# Deskripsi API yang menjelaskan fungsi backend dan teknologi yang digunakan
API_DESCRIPTION = (
    "FastAPI backend for predicting plant failure on agro-environmental conditions. "
    "The backend loads a trained scikit-learn pipeline and exposes prediction endpoints."
)