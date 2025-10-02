FROM python:3.12-slim

# psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY app ./app

EXPOSE 8000

ENV DEV=0

CMD ["/bin/sh", "-c", "if [ \"$DEV\" = \"1\" ]; then \
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload; \
  else \
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000; \
  fi"]
