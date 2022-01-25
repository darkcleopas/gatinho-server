import json
import requests
import pytest


url = 'http://localhost:5000/'
headers = {"Content-Type": "application/json"}

def test_predict():

    # body = json.dumps({"Hello": "hi"})
    
    response = requests.get(url, headers=headers)

    print(response.json())

    assert "result" in response.json()