FROM python:3.7.3

ENV PYTHONUNBUFFERED 1

WORKDIR /web

# install dependecies
COPY requirements.txt /web/requirements.txt
RUN pip install -r requirements.txt
