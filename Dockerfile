FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV DJANGO_DEBUG=False
ENV DB_ENGINE=sqlite

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Run database migrations and collect static files
RUN python manage.py migrate --noinput && python manage.py collectstatic --noinput

EXPOSE 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 dental_builder.wsgi:application
