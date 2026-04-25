import requests
from requests.exceptions import RequestException, Timeout
from config import HEALTH_URL, PREDICT_URL


# Fungsi untuk mengecek status backend dengan memanggil endpoint /health dan mengembalikan status serta informasi respon
def check_backend() -> tuple[bool, dict]:
    """Ping the health endpoint. Returns (is_ok, info_dict)."""
    try:
        r = requests.get(HEALTH_URL, timeout=5)
        if r.status_code == 200:
            return True, r.json()
        return False, {"error": f"HTTP {r.status_code}"}
    except (RequestException, Timeout) as e:
        return False, {"error": str(e)}


# Fungsi untuk mengirim data input ke endpoint /predict dan mengembalikan hasil prediksi dari backend
def call_predict(payload: dict) -> dict:
    """POST payload to /predict. Raises on HTTP error."""
    r = requests.post(PREDICT_URL, json=payload, timeout=20)
    r.raise_for_status()
    return r.json()


# Fungsi untuk mengubah nilai prediksi (0/1) menjadi label yang mudah dipahami oleh pengguna
def format_prediction(prediction: int) -> str:
    return "Risiko Gagal Tumbuh" if prediction == 1 else "Prediksi Tumbuh Baik"


# Fungsi untuk mengkategorikan nilai probabilitas menjadi label confidence (rendah hingga sangat tinggi)
def confidence_label(probability: float | None) -> str:
    if probability is None:
        return "Tidak tersedia"
    if probability >= 0.8:
        return "Sangat Tinggi"
    if probability >= 0.6:
        return "Tinggi"
    if probability >= 0.4:
        return "Sedang"
    return "Rendah"


# Fungsi untuk membangun payload JSON dari input user dengan memastikan tipe data sesuai kebutuhan model (float/int)
def build_payload(
    soil_type, bulk_density, organic_matter_pct, cation_exchange_capacity,
    salinity_ec, buffering_capacity, soil_moisture_pct, moisture_limit_dry,
    moisture_limit_wet, moisture_regime, soil_temp_c, air_temp_c,
    thermal_regime, light_intensity_par, soil_ph, ph_stress_flag,
    nitrogen_ppm, phosphorus_ppm, potassium_ppm, nutrient_balance,
    plant_category,
) -> dict:
    return {
        "soil_type":               soil_type,
        "bulk_density":            float(bulk_density),
        "organic_matter_pct":      float(organic_matter_pct),
        "cation_exchange_capacity": float(cation_exchange_capacity),
        "salinity_ec":             float(salinity_ec),
        "buffering_capacity":      float(buffering_capacity),
        "soil_moisture_pct":       float(soil_moisture_pct),
        "moisture_limit_dry":      float(moisture_limit_dry),
        "moisture_limit_wet":      float(moisture_limit_wet),
        "moisture_regime":         moisture_regime,
        "soil_temp_c":             float(soil_temp_c),
        "air_temp_c":              float(air_temp_c),
        "thermal_regime":          thermal_regime,
        "light_intensity_par":     float(light_intensity_par),
        "soil_ph":                 float(soil_ph),
        "ph_stress_flag":          int(ph_stress_flag),
        "nitrogen_ppm":            float(nitrogen_ppm),
        "phosphorus_ppm":          float(phosphorus_ppm),
        "potassium_ppm":           float(potassium_ppm),
        "nutrient_balance":        nutrient_balance,
        "plant_category":          plant_category,
    }