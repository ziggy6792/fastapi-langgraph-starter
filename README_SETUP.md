# FastAPI Hello World - Getting Started

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. Install Poetry (if not already installed):
```bash
brew install poetry
# or: curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

Poetry will automatically create and manage a virtual environment for you.

### Adding Dependencies

To add a new package (like `pnpm add`):
```bash
poetry add httpx
```

To add a dev dependency:
```bash
poetry add pytest --group dev
```

To remove a package:
```bash
poetry remove httpx
```

## Running the Application

The port is configured in code at `src/config.py`. You can run the application in several ways:

**Option 1: Use the shell script (recommended - handles venv automatically)**
```bash
./run.sh
```

**Option 2: Use Poetry directly**
```bash
poetry run python run.py
```

**Option 3: Activate Poetry shell (then use python normally)**
```bash
poetry shell
python run.py
```

**Option 4: Use uvicorn directly with Poetry**
```bash
poetry run uvicorn src.main:app --reload --port 8001
```

The port (default: 8001) can be changed in `src/config.py` or via environment variable:
```bash
PORT=8002 poetry run python run.py
```

**Default Port**: Port 8001 is configured in `src/config.py` to avoid conflicts with other services (e.g., Docker containers) that may use port 8000.

## Access the Application

- **API**: http://localhost:8001 (or http://127.0.0.1:8001)
- **Hello World Endpoint**: http://localhost:8001/
- **Interactive API Docs (Swagger UI)**: http://localhost:8001/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8001/redoc

## Test the Endpoint

You can test the hello world endpoint using:

```bash
curl http://localhost:8001/
```

Or visit http://localhost:8001/ in your browser.


## What's Next?

This is a minimal FastAPI application. As you learn more, you can:
- Add more endpoints
- Use Pydantic models for request/response validation
- Add dependencies for authentication, validation, etc.
- Structure your code by domain (as shown in the main README.md)
