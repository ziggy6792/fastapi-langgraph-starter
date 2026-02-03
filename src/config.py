"""Application configuration."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application settings."""
    
    PORT: int = 8002
    HOST: str = "127.0.0.1"
    RELOAD: bool = True  # Enable auto-reload in development
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",  # Ignore extra fields from .env (like OPENAI_API_KEY used by AI domain)
    )


settings = Config()
