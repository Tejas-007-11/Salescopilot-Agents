import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_churn(data_dict):
    df = pd.DataFrame([data_dict])

    df = pd.get_dummies(df)

    # align columns with training
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df:
            df[col] = 0

    df = df[model_features]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return prediction, round(probability, 2)