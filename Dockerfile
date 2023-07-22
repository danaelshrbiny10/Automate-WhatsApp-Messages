FROM python:3.8-slim-buster

# Install PostgreSQL development libraries and other required packages
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install dotenv
RUN pip install --no-cache-dir python-dotenv

# Set the working directory inside the container
WORKDIR /app

# Copy requirements files
COPY requirements /app/requirements

# Install pip and setuptools
RUN pip install --upgrade pip setuptools

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements files
COPY requirements/base.txt requirements/local.txt ./

# Install Base requirements
RUN pip install --no-cache-dir -r requirements/base.txt

# Install Local requirements
RUN pip install --no-cache-dir -r requirements/local.txt


# Copy the project files
COPY . .

# Install gunicorn
RUN pip install gunicorn

# Start the services
CMD celery -A config.celery worker --pool=solo -l info & \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Show all installed packages
RUN pip freeze
