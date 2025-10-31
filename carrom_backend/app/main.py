from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users_router, games_router

openapi_tags = [
    {"name": "Health", "description": "Service health and meta endpoints."},
    {"name": "Users", "description": "User management endpoints."},
    {"name": "Games", "description": "Game management endpoints."},
]

app = FastAPI(
    title="Carrom Backend API",
    description="FastAPI backend for Carrom game management with users and games endpoints.",
    version="0.1.0",
    openapi_tags=openapi_tags,
)

# CORS (open during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get(
    "/health",
    tags=["Health"],
    summary="Health check",
    description="Simple health check endpoint.",
)
def health():
    """Health check endpoint that returns a simple JSON response."""
    return {"status": "ok"}


# Include routers
app.include_router(users_router)
app.include_router(games_router)
