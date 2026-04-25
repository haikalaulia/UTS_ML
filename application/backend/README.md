# Agro Environmental Prediction Backend

FastAPI backend for serving a trained machine learning pipeline that predicts `failure_flag` from agro-environmental inputs.

## Run

```bash
pip install -r requirements.txt
uvicorn agro_backend_app.main:app --reload
```

If your model file uses a different name or location, set:

```bash
export MODEL_PATH="/path/to/your/model.pkl"
```

## Endpoints

- `GET /` → service info
- `GET /health` → model health check
- `POST /predict` → single prediction
- `POST /predict-batch` → batch prediction
