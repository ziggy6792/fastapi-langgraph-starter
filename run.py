"""Run the FastAPI application."""
from pathlib import Path

import uvicorn

from src.config import settings

if __name__ == "__main__":
    # Get the project root directory
    project_root = Path(__file__).parent
    
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        reload_dirs=[str(project_root / "src")] if settings.RELOAD else None,
    )
