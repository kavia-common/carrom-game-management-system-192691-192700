from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, status


from app.models import User, UserCreate, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage (placeholder). In production, replace with database layer.
_USERS: List[User] = []
_USER_ID_SEQ: int = 1


def _next_user_id() -> int:
    global _USER_ID_SEQ
    nid = _USER_ID_SEQ
    _USER_ID_SEQ += 1
    return nid


# PUBLIC_INTERFACE
@router.get(
    "",
    summary="List users",
    description="Returns a list of all users in the system.",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
)
def list_users():
    """List all users currently stored (in-memory)."""
    return _USERS


# PUBLIC_INTERFACE
@router.post(
    "",
    summary="Create user",
    description="Create a new user with a unique username.",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
def create_user(payload: UserCreate):
    """Create a new user."""
    if any(u.username == payload.username for u in _USERS):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    user = User(
        id=_next_user_id(),
        username=payload.username,
        name=payload.name,
        email=payload.email,
        created_at=datetime.utcnow(),
    )
    _USERS.append(user)
    return user


# PUBLIC_INTERFACE
@router.get(
    "/{user_id}",
    summary="Get user",
    description="Get a user by ID.",
    response_model=User,
)
def get_user(user_id: int):
    """Retrieve a user by its ID."""
    for u in _USERS:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


# PUBLIC_INTERFACE
@router.put(
    "/{user_id}",
    summary="Update user",
    description="Update fields of a user by ID.",
    response_model=User,
)
def update_user(user_id: int, payload: UserUpdate):
    """Update an existing user."""
    for idx, u in enumerate(_USERS):
        if u.id == user_id:
            # Validation for unique username if provided
            if payload.username and payload.username != u.username:
                if any(other.username == payload.username for other in _USERS):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Username already exists",
                    )
            updated = u.model_copy(update=payload.model_dump(exclude_unset=True))
            _USERS[idx] = updated
            return updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


# PUBLIC_INTERFACE
@router.delete(
    "/{user_id}",
    summary="Delete user",
    description="Delete a user by ID.",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: int):
    """Delete a user by its ID."""
    for idx, u in enumerate(_USERS):
        if u.id == user_id:
            del _USERS[idx]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
