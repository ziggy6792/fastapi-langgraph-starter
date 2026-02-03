"""AI domain Pydantic schemas."""
from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request schema for chat endpoint."""
    
    message: str = Field(min_length=1, description="User message to send to LLM")


class ChatResponse(BaseModel):
    """Response schema for chat endpoint."""
    
    response: str = Field(description="LLM generated response")


class ThreadCreateResponse(BaseModel):
    """Response schema for thread creation."""
    
    threadId: UUID = Field(description="Unique identifier for the conversation thread")


class ThreadChatRequest(BaseModel):
    """Request schema for thread chat endpoint."""
    
    message: str = Field(min_length=1, description="User message to send to LLM")
