from __future__ import annotations

from typing import List
from pydantic import BaseModel, Field


# Model input utama untuk satu data prediksi, lengkap dengan validasi dan deskripsi tiap fitur
class PredictionInput(BaseModel):
    soil_type: str = Field(..., examples=["Clayey", "Alluvial"])
    bulk_density: float = Field(..., ge=0, description="Bulk density of soil")
    organic_matter_pct: float = Field(..., ge=0, description="Organic matter percentage")
    cation_exchange_capacity: float = Field(..., ge=0, description="CEC")
    salinity_ec: float = Field(..., ge=0, description="Electrical conductivity")
    buffering_capacity: float = Field(..., ge=0, description="Soil buffering capacity")
    soil_moisture_pct: float = Field(..., ge=0, description="Soil moisture percentage")
    moisture_limit_dry: float = Field(..., ge=0, description="Dry moisture threshold")
    moisture_limit_wet: float = Field(..., ge=0, description="Wet moisture threshold")
    moisture_regime: str = Field(..., examples=["dry", "optimal", "wet"])
    soil_temp_c: float = Field(..., description="Soil temperature in Celsius")
    air_temp_c: float = Field(..., description="Air temperature in Celsius")
    thermal_regime: str = Field(..., examples=["optimal", "heat_stress", "cold_stress"])
    light_intensity_par: float = Field(..., ge=0, description="PAR light intensity")
    soil_ph: float = Field(..., ge=0, le=14, description="Soil pH")
    ph_stress_flag: int = Field(..., ge=0, le=1, description="pH stress indicator")
    nitrogen_ppm: float = Field(..., ge=0, description="Nitrogen in ppm")
    phosphorus_ppm: float = Field(..., ge=0, description="Phosphorus in ppm")
    potassium_ppm: float = Field(..., ge=0, description="Potassium in ppm")
    nutrient_balance: str = Field(..., examples=["optimal", "excessive", "deficient"])
    plant_category: str = Field(..., examples=["vegetable", "fruit", "cereal"])


# Model input untuk prediksi batch (multiple data sekaligus dalam satu request)
class BatchPredictionInput(BaseModel):
    items: List[PredictionInput]


# Model response untuk satu hasil prediksi, berisi label, nilai prediksi, dan probabilitas (opsional)
class PredictionResponse(BaseModel):
    prediction: int
    predicted_label: str
    probability_failure: float | None = None


# Model response untuk hasil prediksi batch (list dari beberapa hasil prediksi)
class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]


# Model request alternatif tanpa validasi detail (biasanya digunakan untuk kebutuhan internal atau fleksibilitas input)
class PredictionRequest(BaseModel):
    soil_type: str
    bulk_density: float
    organic_matter_pct: float
    cation_exchange_capacity: float
    salinity_ec: float
    buffering_capacity: float
    soil_moisture_pct: float
    moisture_limit_dry: float
    moisture_limit_wet: float
    moisture_regime: str
    soil_temp_c: float
    air_temp_c: float
    thermal_regime: str
    light_intensity_par: float
    soil_ph: float
    ph_stress_flag: int
    nitrogen_ppm: float
    phosphorus_ppm: float
    potassium_ppm: float
    nutrient_balance: str
    plant_category: str