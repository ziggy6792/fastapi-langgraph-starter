"""User domain exceptions."""
from fastapi import HTTPException, status


class UserNotFound(HTTPException):
    """Raised when a user is not found."""
    
    def __init__(self, user_id: str) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )


class UserEmailAlreadyExists(HTTPException):
    """Raised when trying to create a user with an existing email."""
    
    def __init__(self, email: str) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email {email} already exists"
        )
