from fastapi import FastAPI

app = FastAPI(title="FastAPI Hello World")


@app.get("/")
async def hello_world() -> dict[str, str]:
    """Simple hello world endpoint."""
    return {"message": "Hello, World!!"}
