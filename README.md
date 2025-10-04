# URL Shortener

A simple URL shortener built using FastAPI and PostgreSQL

# Requirements

### Manual installation:

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/)
- PostgreSQL instance

### Docker:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

# Setup (without Docker)

### 1. Clone the repository:

```bash
$ git clone https://github.com/greatlolz/url-shortener.git
$ cd url-shortener
```

### 2. Install dependencies:

```bash
$ poetry install
```

### 3. Setup database:

Create a user and database for the application in your PostgreSQL instance.

### 4. Set environment variables:

```bash
DATABASE_URL=postgresql+psycopg2://<db_user>:<db_password>@<db_host>:5432/<db_name>
```

### 5. Apply database migrations:

```bash
$ poetry run alembic upgrade head
```

### 6. Run the application:

```bash
$ poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

or run with hot reloading:

```bash
$ poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

# Setup (with Docker)

### 1. Clone the repository:

```bash
$ git clone https://github.com/greatlolz/url-shortener.git
$ cd url-shortener
```

### 2. Set environment variables:
(either create a .env file or set the variables in your environment)

```bash
DEV=1 # optional, enables workspace reloading

POSTGRES_USER=<db_user>
POSTGRES_PASSWORD=<db_password>
POSTGRES_DB=<db_name>

DATABASE_URL=postgresql+psycopg2://<db_user>:<db_password>@db:5432/<db_name>
```

### 3. Run the application:

```bash
$ docker compose up -d
```

# Usage & Documentation

After running the application, you can access OpenAPI (Swagger) documentation at the `/docs` endpoint. \
Alternatively, you can access the ReDoc documentation at the `/redoc` endpoint.

### Endpoints

- `POST /shorten` -  Shorten a URL \
    - Request body: 
        ```json
        {
            "original_url": "http://example.com"
        }
        ```
    - Response: 
        ```json
        {
            "id": 1,
            "original_url": "http://example.com",
            "short_url": "abc123"
        }
        ```
- `GET /{short_url}` - Redirect to the original URL
    - Response: HTTP 307 Temporary Redirect
    
- `GET /{short_url}/info` - Get information about the shortened URL
    - Response: 
        ```json
        {
            "original_url": "http://example.com",
            "short_url": "abc123",
            "clicks": 1,
            "created_at": "2025-01-01T00:00:00.000Z"
        }
        ```

# License

This project is licensed under the MIT License.


