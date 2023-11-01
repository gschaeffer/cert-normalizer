FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt

CMD exec gunicorn --bind 0.0.0.0:8080 --workers 2 --threads 4 wsgi:app
