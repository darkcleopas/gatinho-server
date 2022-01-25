import json
import requests
import pytest
import base64

url = 'http://localhost:5000/predict'
headers = {"Content-Type": "application/json"}

def test_cat_predict():

    with open("tests/cat1.jpg", "rb") as f:
        img_bytes = f.read()       

    img_b64 = base64.b64encode(img_bytes).decode("utf8")
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    payload = json.dumps({"image": img_b64})

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

    assert response.json()["is_cat"] == True


def test_not_cat_predict():

    with open("tests/notcat1.jpeg", "rb") as f:
        img_bytes = f.read()       

    img_b64 = base64.b64encode(img_bytes).decode("utf8")
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    payload = json.dumps({"image": img_b64})

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

    assert response.json()["is_cat"] == False