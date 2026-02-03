"""AI domain Pydantic schemas."""
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request schema for chat endpoint."""
    
    message: str = Field(min_length=1, description="User message to send to LLM")


class ChatResponse(BaseModel):
    """Response schema for chat endpoint."""
    
    response: str = Field(description="LLM generated response")
