FROM python:3.11-slim-buster

RUN apt-get update 

ENV PATH="/usr/lib/postgresql/12/bin:$PATH"


WORKDIR /app

COPY src/ .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Install gunicorn
RUN pip3 install gunicorn



CMD celery -A config.celery worker --pool=solo -l info & \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
