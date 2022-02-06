<p align="center">

  <h3 align="center">Gatinho!</h3>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Lincense&message=MIT&color=0000ff " alt="License" />
</p>

<p align="center">
    This site was created to obtain parcial grade in Distributed Systems subject
    <br />
    <br />
    <a href="README.md">🇺🇸English</a>
    ·
    <a href="README-pt.md">🇧🇷Portuguese</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## 🗂 Table of Contents

* [About the Project](#book-about-the-project)
* [Installation](#bricks-installation)
  * [Prerequisites](#construction-prerequisites)
  * [Front-end](#lipstick-front-end)
    * [Installing Dependencies](#construction-installing-dependencies)
    * [Running Project](#arrow_forward-running-project)
* [License](#page_facing_up-license)
* [Authors](#woman_technologist-man_technologist-authors)

## :book: About The Project

The project is to use image processing with Python ([repository is here](https://github.com/DarkCleopas/gatinho)), where you can send a image to check if it is a cat or not.

## :bricks: Installation

This project uses [Python](https://www.python.org/) and [Docker](https://www.docker.com/), you will need them to build its dependencies.

### :construction: Prerequisites

Clone the project

```sh
git clone https://github.com/DarkCleopas/gatinho.git

cd gatinho/

```

🚨 If you don't have git in your machine, you can install it [here](https://git-scm.com/downloads).

### :arrow_forward: Running Project

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

## :page_facing_up: License

This project uses [MIT](https://github.com/3salles/guess-kitty/blob/main/LICENSE) license.

## :woman_technologist: :man_technologist: Authors

[Beatriz Salles](https://github.com/3salles)
<br/>
[Lucas Cléopas](https://github.com/DarkCleopas)



<p align="center">Developed with 💜</p>
