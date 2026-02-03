"""User API routes."""
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.users.dependencies import valid_user_id
from src.users.schemas import UserCreate, UserResponse, UserUpdate
from src.users.service import user_repository

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    description="Create a new user",
    summary="Create User",
)
async def create_user(user_data: UserCreate) -> dict[str, Any]:
    """Create a new user."""
    user = await user_repository.create(user_data)
    return user


@router.get(
    "",
    response_model=list[UserResponse],
    description="Get all users",
    summary="List Users",
)
async def list_users() -> list[dict[str, Any]]:
    """Get all users."""
    users = await user_repository.get_all()
    return users


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    description="Get a user by ID",
    summary="Get User",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
    },
)
async def get_user(
    user:UserResponse = Depends(valid_user_id)
):
    """Get a user by ID."""
    return user
    
@router.get(
    "/mock/{user_id}",
    response_model=UserResponse,
    description="Get a user by ID",
    summary="Get User",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
    },
)
async def mock_user(
    user_id: UUID
):
    """Get a user by ID."""
    return UserResponse(
        id=user_id,  # 👈 id comes from the URL
        firstName="John",
        lastName="Doe",
        email="john.doe@example.com",
        createdAt=datetime.now(timezone.utc),  # 👈 timezone-aware
    )

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    description="Update a user",
    summary="Update User",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
        status.HTTP_409_CONFLICT: {"description": "Email already exists"},
    },
)
async def update_user(
    user_data: UserUpdate,
    user: dict[str, Any] = Depends(valid_user_id),
) -> dict[str, Any]:
    """Update a user."""
    user_id = UUID(user["id"])
    updated_user = await user_repository.update(user_id, user_data)
    return updated_user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete a user",
    summary="Delete User",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
    },
)
async def delete_user(
    user: dict[str, Any] = Depends(valid_user_id),
) -> None:
    """Delete a user."""
    user_id = UUID(user["id"])
    await user_repository.delete(user_id)
