# gatinho

# Installation

Clone the project

```sh
git clone https://github.com/DarkCleopas/gatinho.git

cd gatinho/
```

There are two ways to set up this project locally

## Using Docker

Creating a Docker container for Gatinho server

```sh
sudo docker build -t gatinho/server .
```

Run the gatinho/server container

```sh
sudo docker run -d --name gatinho-server --network host gatinho/server
```

Run the tests
```sh
python -m pytest tests/test_iris.py
```

## Directly in the terminal

Install the dependencies and run the server

```sh
pip install -r requirements.txt
 
python gatinho_server.py
```

Run the tests
```sh
python -m pytest tests/test_iris.py
```


# Usage

Gatinho is a REST API that can be used through HTTP requests.

## Make a Gatinho prediction

`POST localhost:5000/predict`
### Request

There is only one parameter to send. `"image"` expected a base 64 code from the image that will be send.
You can use [this site](https://base64.guru/converter/encode/image) to get the base64 code of an image.

```json
{
    "image": "base64 code"
}
```

### Response
```json
{
    "score": 1.0, 
    "is_cat": true
}
```
