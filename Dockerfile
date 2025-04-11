FROM python:3.12-slim

WORKDIR /usr/src/app/bot

COPY requirements.txt /usr/src/app/bot

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
