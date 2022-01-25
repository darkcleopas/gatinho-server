from fastapi import FastAPI, HTTPException, Depends, Request
import uvicorn

app = FastAPI()

@app.get('/')
def predict():

    # data = request.data

    # print(data)

    return {"result": "oi"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)