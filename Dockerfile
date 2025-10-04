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

COPY migrations ./migrations
COPY alembic.ini ./

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
