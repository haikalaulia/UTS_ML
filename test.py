import joblib

model = joblib.load("model/random_forest_tuned_pipeline.pkl")
print(model)