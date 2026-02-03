"""AI router dependencies."""
from uuid import UUID

from fastapi import HTTPException, status

from src.ai.service import thread_repository


async def valid_thread_id(thread_id: UUID) -> UUID:
    """
    Dependency to validate thread exists.
    
    Can be reused across multiple endpoints that need a valid thread.
    """
    exists = await thread_repository.thread_exists(thread_id)
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Thread with id {thread_id} not found"
        )
    
    return thread_id
