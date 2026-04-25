import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from .services import ModelService
from .schemas import PredictionRequest

# Konfigurasi logging untuk mencatat aktivitas aplikasi (info, error, dll)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Menentukan path root project dan lokasi file model machine learning
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "model" / "random_forest_tuned_pipeline.pkl"

# Inisialisasi service yang bertanggung jawab untuk loading model dan prediksi
model_service = ModelService(MODEL_PATH)

# Inisialisasi aplikasi FastAPI beserta metadata (judul, versi, deskripsi)
app = FastAPI(
    title="Agro ML API",
    version="1.0.0",
    description="API untuk prediksi kegagalan tanaman"
)

# Konfigurasi CORS agar frontend (misalnya Streamlit) dapat mengakses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production: ganti domain spesifik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event startup untuk memuat model saat aplikasi pertama kali dijalankan
@app.on_event("startup")
def startup_event():
    logger.info("🚀 Starting application...")
    try:
        model_service.load_model()
    except Exception as e:
        logger.error(f"Startup failed: {e}")

# Endpoint untuk mengecek status backend dan kesiapan model
@app.get("/health")
def health_check():
    if model_service.is_ready():
        return {"status": "ok", "model_loaded": True}
    else:
        return {
            "status": "degraded",
            "model_loaded": False,
            "error": "Model not loaded"
        }

# Endpoint utama untuk menerima input data dan mengembalikan hasil prediksi dari model
@app.post("/predict")
def predict(request: PredictionRequest):
    if not model_service.is_ready():
        raise HTTPException(status_code=503, detail="Model not ready")

    try:
        result = model_service.predict(request.dict())
        return result

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        logger.exception("Unexpected error")
        raise HTTPException(status_code=500, detail="Internal Server Error")