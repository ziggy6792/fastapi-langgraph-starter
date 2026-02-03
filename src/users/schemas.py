"""User Pydantic schemas."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema with common fields."""
    
    firstName: str = Field(min_length=1, max_length=128, description="User's first name")
    lastName: str = Field(min_length=1, max_length=128, description="User's last name")
    email: EmailStr = Field(description="User's email address")


class UserCreate(UserBase):
    """Schema for creating a new user."""
    pass


class UserUpdate(BaseModel):
    """Schema for updating a user (all fields optional)."""
    
    firstName: str | None = Field(None, min_length=1, max_length=128)
    lastName: str | None = Field(None, min_length=1, max_length=128)
    email: EmailStr | None = None


class UserResponse(UserBase):
    """Schema for user response."""
    
    id: UUID = Field(description="User's unique identifier")
    createdAt: datetime = Field(description="User creation timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "firstName": "John",
                "lastName": "Doe",
                "email": "john.doe@example.com",
                "createdAt": "2024-01-01T00:00:00Z"
            }
        }
