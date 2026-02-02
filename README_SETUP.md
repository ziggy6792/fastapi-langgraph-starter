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

Start the FastAPI server using uvicorn:

```bash
uvicorn src.main:app --reload
```

The `--reload` flag enables auto-reload on code changes (useful for development).

## Access the Application

- **API**: http://localhost:8000
- **Hello World Endpoint**: http://localhost:8000/
- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc

## Test the Endpoint

You can test the hello world endpoint using:

```bash
curl http://localhost:8000/
```

Or visit http://localhost:8000/ in your browser.

## What's Next?

This is a minimal FastAPI application. As you learn more, you can:
- Add more endpoints
- Use Pydantic models for request/response validation
- Add dependencies for authentication, validation, etc.
- Structure your code by domain (as shown in the main README.md)
