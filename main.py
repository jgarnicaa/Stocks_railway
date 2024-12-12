from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

# Reemplace esto con su implementación:
class ApiInput(BaseModel):
    ### ESCRIBA SU CÓDIGO AQUÍ ###
    features: List[float]

# Reemplace esto con su implementación:
class ApiOutput(BaseModel):
    ### ESCRIBA SU CÓDIGO AQUÍ ###
    forecast: float

app = FastAPI()
model = joblib.load("model.joblib")

# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    prediction = model.predict([data.features])
    preds = ApiOutput(forecast=prediction)
