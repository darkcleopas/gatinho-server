FROM python:3.7-slim-bullseye

WORKDIR /app
COPY . ./

RUN apt-get update -y

RUN apt-get install libglib2.0-0 libsm6 libxrender1 libxext6 libmagic-dev ffmpeg poppler-utils -y

RUN python3 -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r ./requirements.txt

CMD python3 gatinho_server.py

# EXPOSE 5000

