import logging
from pathlib import Path
import joblib
import pandas as pd
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Service utama untuk menangani loading model dan proses prediksi menggunakan model machine learning
class ModelService:
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.model = None

    # Method untuk memuat model dari file .pkl menggunakan joblib, dengan handling error jika gagal
    def load_model(self):
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")

        try:
            self.model = joblib.load(self.model_path)
            logger.info("✅ Model loaded successfully")
        except Exception as e:
            logger.exception("❌ Failed to load model")
            raise RuntimeError(f"Failed to load model: {e}")

    # Method untuk mengecek apakah model sudah berhasil dimuat dan siap digunakan
    def is_ready(self) -> bool:
        return self.model is not None

    # Method utama untuk melakukan prediksi berdasarkan input data dan mengembalikan hasil prediksi serta probabilitas
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.is_ready():
            raise RuntimeError("Model is not loaded")

        try:
            df = pd.DataFrame([data])

            prediction = self.model.predict(df)[0]

            if hasattr(self.model, "predict_proba"):
                probability = float(self.model.predict_proba(df)[0][1])
            else:
                probability = None

            return {
                "prediction": int(prediction),
                "probability": probability
            }

        except Exception as e:
            logger.exception("❌ Prediction failed")
            raise RuntimeError(f"Prediction error: {e}")