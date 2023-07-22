FROM python:3.8-slim-buster

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

# Copy requirements files and install dependencies
COPY requirements/base.txt requirements/local.txt ./
RUN pip3 install --no-cache-dir -r base.txt -r local.txt

# Copy the project files
COPY . .

# Install gunicorn
RUN pip3 install gunicorn

CMD celery -A config.celery worker --pool=solo -l info & \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
