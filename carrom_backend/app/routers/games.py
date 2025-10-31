from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.models import Game, GameCreate, GameUpdate

router = APIRouter(
    prefix="/games",
    tags=["Games"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage (placeholder). Replace with DB in production.
_GAMES: List[Game] = []
_GAME_ID_SEQ: int = 1


def _next_game_id() -> int:
    global _GAME_ID_SEQ
    nid = _GAME_ID_SEQ
    _GAME_ID_SEQ += 1
    return nid


# PUBLIC_INTERFACE
@router.get(
    "",
    summary="List games",
    description="Returns a list of all games.",
    response_model=List[Game],
)
def list_games():
    """List all games currently stored (in-memory)."""
    return _GAMES


# PUBLIC_INTERFACE
@router.post(
    "",
    summary="Create game",
    description="Create a new game with specified players and initial status.",
    response_model=Game,
    status_code=status.HTTP_201_CREATED,
)
def create_game(payload: GameCreate):
    """Create a new game."""
    game = Game(
        id=_next_game_id(),
        players=payload.players,
        status=payload.status,
        score=payload.score or {},
        created_at=datetime.utcnow(),
    )
    _GAMES.append(game)
    return game


# PUBLIC_INTERFACE
@router.get(
    "/{game_id}",
    summary="Get game",
    description="Get a game by ID.",
    response_model=Game,
)
def get_game(game_id: int):
    """Retrieve a game by its ID."""
    for g in _GAMES:
        if g.id == game_id:
            return g
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")


# PUBLIC_INTERFACE
@router.put(
    "/{game_id}",
    summary="Update game",
    description="Update fields of a game by ID.",
    response_model=Game,
)
def update_game(game_id: int, payload: GameUpdate):
    """Update an existing game."""
    for idx, g in enumerate(_GAMES):
        if g.id == game_id:
            updated = g.model_copy(update=payload.model_dump(exclude_unset=True))
            _GAMES[idx] = updated
            return updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")


# PUBLIC_INTERFACE
@router.delete(
    "/{game_id}",
    summary="Delete game",
    description="Delete a game by ID.",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_game(game_id: int):
    """Delete a game by its ID."""
    for idx, g in enumerate(_GAMES):
        if g.id == game_id:
            del _GAMES[idx]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
