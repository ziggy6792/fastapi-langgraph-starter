"""AI domain configuration."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class AIConfig(BaseSettings):
    """AI-specific settings."""
    
    OPENAI_API_KEY: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


ai_settings = AIConfig()
