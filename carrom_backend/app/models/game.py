from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class GameBase(BaseModel):
    """Base fields for a game."""
    players: List[int] = Field(..., description="List of user IDs participating in the game")
    status: str = Field("pending", description="Current status of the game: pending|active|completed")
    score: Optional[Dict[int, int]] = Field(default_factory=dict, description="Mapping of user ID to score")


class GameCreate(GameBase):
    """Payload to create a new game."""
    pass


class GameUpdate(BaseModel):
    """Payload to update a game."""
    players: Optional[List[int]] = Field(None, description="Updated list of players")
    status: Optional[str] = Field(None, description="Updated status")
    score: Optional[Dict[int, int]] = Field(None, description="Updated score mapping")


class Game(GameBase):
    """Game model returned by the API, includes generated fields."""
    id: int = Field(..., description="Unique identifier for the game")
    created_at: datetime = Field(..., description="Timestamp when the game was created")
