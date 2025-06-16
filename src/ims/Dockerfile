FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc \
    libmemcached-dev zlib1g-dev libjpeg-dev libssl-dev libffi-dev \
    && pip install --upgrade pip

# Copy requirements & install
COPY requirement.txt .
RUN pip install -r requirement.txt

# Copy project
COPY . .

# Replace local config with container config
RUN rm config/env.json && cp config/docker_env.json config/env.json

# Collect static (optional)
RUN python manage.py collectstatic --noinput

# Run the app using gunicorn
CMD ["gunicorn", "ims.wsgi:application", "--config", "docker/gunicorn_conf.py"]
