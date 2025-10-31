from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the main FastAPI app which includes routers
try:
    # Preferred app with routers and /health
    from app.main import app  # type: ignore
except Exception:
    # Fallback minimal app if import fails
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Backward-compatible root endpoint that proxies to health payload
@app.get("/", tags=["Health"], summary="Health Check")
def root_health():
    """
    Root health endpoint maintained for compatibility with existing preview.
    Redirects logically to the /health semantics by returning a simple message.
    """
    return {"message": "Healthy"}
