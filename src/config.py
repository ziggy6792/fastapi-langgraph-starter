"""Application configuration."""
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Application settings."""
    
    PORT: int = 8002
    HOST: str = "127.0.0.1"
    RELOAD: bool = True  # Enable auto-reload in development
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Config()
