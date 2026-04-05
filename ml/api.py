from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel, Field

class ChurnRequest(BaseModel):
    tenure: int = Field(example=5)
    monthlycharges: float = Field(example=70)
    totalcharges: float = Field(example=300)
    tenure_group: str = Field(example="new")

app = FastAPI()

# load model
model = joblib.load(r"C:\Customer Churn Pipeline\customer_churn_pipeline\ml\model.joblib")
features = joblib.load(r"C:\Customer Churn Pipeline\customer_churn_pipeline\ml\features.joblib")

@app.get("/")
def home():
    return {"message": "Churn Prediction API 🚀"}
    
@app.post("/predict")
def predict(data: ChurnRequest):

    df = pd.DataFrame([data.dict()])

    # preprocessing
    df = pd.get_dummies(df, drop_first=True)

    # samakan fitur
    df = df.reindex(columns=features, fill_value=0)

    prediction = model.predict(df)[0]

    return {
        "churn_prediction": int(prediction)
    }