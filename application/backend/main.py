from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

# =========================
# Config Path
# =========================
MODEL_PATH = 
# Jika menggunakan pipeline (sudah include preprocessing)
#PREPROCESSOR_PATH = 

model = None
preprocessor = None
use_pipeline = False

# =========================
# Load Model
# =========================
try:
    if os.path.exists(MODEL_PATH):
        model = 

        # Cek apakah ini pipeline (punya step transform)
        if hasattr(model, "predict") and hasattr(model, "transform") is False:
            use_pipeline = True

    if os.path.exists(PREPROCESSOR_PATH):
        preprocessor = 

except Exception as e:
    print("Error loading model:", e)


# =========================
# Request Schema
# =========================
class InputData(BaseModel):
    # Sesuaikan pada saat training kolom apa saja yang digunakan
    bulk_density: float
    organic_matter: float
    cation_exchange_capacity: float
    salinity: float
    


# =========================
# Root Endpoint
# =========================
@app.get("/")
def read_root():
    return {"message": "Agro ML API is running"}


# =========================
# Prediction Endpoint
# =========================
@app.post("/predict")
def predict(data: InputData):

    if model is None:
        return {"error": "Model not loaded"}

    try:
        # Convert ke numpy array
        input_array = np.array([[
            
        ]])

        # =========================
        # MODE 1: Pipeline
        # =========================
        if use_pipeline:
            prediction = 

        # =========================
        # MODE 2: Manual preprocessing
        # =========================
        else:
    
            prediction = 

        return {
            "prediction": int(prediction),
            "interpretation": "Suitable" if prediction == 1 else "Not Suitable"
        }

    except Exception as e:
        return {"error": str(e)}
