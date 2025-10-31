from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    """Base fields for a user."""
    username: str = Field(..., description="Unique username of the user")
    name: Optional[str] = Field(None, description="Full name of the user")
    email: Optional[EmailStr] = Field(None, description="Email address of the user")


class UserCreate(UserBase):
    """Payload for creating a new user."""
    pass


class UserUpdate(BaseModel):
    """Payload for updating existing user fields."""
    username: Optional[str] = Field(None, description="New username")
    name: Optional[str] = Field(None, description="New full name")
    email: Optional[EmailStr] = Field(None, description="New email address")


class User(UserBase):
    """User model returned by the API, includes generated fields."""
    id: int = Field(..., description="Unique identifier for the user")
    created_at: datetime = Field(..., description="Timestamp when the user was created")
