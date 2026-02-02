# FastAPI Hello World - Getting Started

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

The port is configured in code at `src/config.py`. You can run the application in several ways:

**Option 1: Use the shell script (recommended - handles venv automatically)**
```bash
./run.sh
```

**Option 2: Use the Python run script directly**
```bash
python3 run.py
```

**Note**: If you have a shell alias for `python` that points to the system Python, use `python3` instead, or use `./run.sh` which automatically uses the venv's Python interpreter.

**Option 2: Use the shell script**
```bash
./run.sh
```

**Option 3: Use uvicorn directly**
```bash
uvicorn src.main:app --reload --port 8001
```

The port (default: 8001) can be changed in `src/config.py` or via environment variable:
```bash
PORT=8002 python run.py
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
