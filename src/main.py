from fastapi import FastAPI

from src.ai import router as ai_router
from src.users import router as users_router

app = FastAPI(title="FastAPI Best Practices")

# Include routers
app.include_router(users_router.router)
app.include_router(ai_router.router)


@app.get("/")
async def hello_world() -> dict[str, str]:
    """Simple hello world endpoint."""
    return {"message": "Hello, World!!"}
