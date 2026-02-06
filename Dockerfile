## Base Image

FROM python:3.11-slim

## Python Optimization


ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

## Working Directory app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "resume-builder.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
