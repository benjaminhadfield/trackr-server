FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . /code/
RUN pip install -r requirements/prod.txt
