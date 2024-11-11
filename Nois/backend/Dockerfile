# Dockerfile for Django backend
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./jwt_private.pem /code/backend/jwt_private.pem
COPY ./jwt_public.pem /code/backend/jwt_public.pem
COPY . /code/

EXPOSE 8000
