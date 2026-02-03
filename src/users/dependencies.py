"""User router dependencies."""
from typing import Any
from uuid import UUID

from fastapi import Depends

from src.users import exceptions
from src.users.service import user_repository


async def valid_user_id(user_id: UUID) -> dict[str, Any]:
    """
    Dependency to validate user exists.
    
    Can be reused across multiple endpoints that need a valid user.
    """
    user = await user_repository.get_by_id(user_id)
    if not user:
        raise exceptions.UserNotFound(str(user_id))
    
    return user
