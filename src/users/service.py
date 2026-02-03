"""User service (repository pattern for in-memory storage)."""
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from src.users import exceptions
from src.users.schemas import UserCreate, UserUpdate


class UserRepository:
    """In-memory user repository (similar to NestJS repository pattern)."""
    
    def __init__(self) -> None:
        """Initialize with empty storage."""
        self._users: dict[UUID, dict[str, Any]] = {}
    
    async def create(self, user_data: UserCreate) -> dict[str, Any]:
        """Create a new user."""
        # Check if email already exists
        for user in self._users.values():
            if user["email"] == user_data.email:
                raise exceptions.UserEmailAlreadyExists(user_data.email)
        
        # Create user
        user_id = uuid4()
        now = datetime.now(timezone.utc)
        
        user = {
            "id": str(user_id),
            "firstName": user_data.firstName,
            "lastName": user_data.lastName,
            "email": user_data.email,
            "createdAt": now,
        }
        
        self._users[user_id] = user
        return user
    
    async def get_by_id(self, user_id: UUID) -> dict[str, Any] | None:
        """Get a user by ID."""
        return self._users.get(user_id)
    
    async def get_all(self) -> list[dict[str, Any]]:
        """Get all users."""
        return list(self._users.values())
    
    async def update(self, user_id: UUID, user_data: UserUpdate) -> dict[str, Any]:
        """Update a user."""
        user = await self.get_by_id(user_id)
        if not user:
            raise exceptions.UserNotFound(str(user_id))
        
        # Check if email is being updated and already exists
        if user_data.email and user_data.email != user["email"]:
            for existing_user in self._users.values():
                if existing_user["email"] == user_data.email and existing_user["id"] != str(user_id):
                    raise exceptions.UserEmailAlreadyExists(user_data.email)
        
        # Update fields
        update_data = user_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            user[key] = value
        
        self._users[user_id] = user
        return user
    
    async def delete(self, user_id: UUID) -> None:
        """Delete a user."""
        user = await self.get_by_id(user_id)
        if not user:
            raise exceptions.UserNotFound(str(user_id))
        
        del self._users[user_id]


# Singleton instance (similar to NestJS service injection)
user_repository = UserRepository()
