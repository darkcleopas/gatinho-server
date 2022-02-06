import json                    
from fastapi import FastAPI, HTTPException, Depends, Request
import uvicorn
from src.model.load_model import load_model
import src.routes.predict as cat_predict

from pydantic import BaseModel

class CatPrediction(BaseModel):
    image: str


model = load_model("src/model/")

app = FastAPI()


@app.post('/predict')
def predict(content: CatPrediction):

    img_b64 = content.image.split(",")[-1]

    result = cat_predict.handler(model, img_b64)

    print(result)

    return result



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)