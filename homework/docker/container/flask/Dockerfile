FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip python3

COPY ./app.py /app/app.py
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ['python']
CMD ['app.py']