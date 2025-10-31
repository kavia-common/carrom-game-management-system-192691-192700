# carrom-game-management-system-192691-192700

Carrom Backend (FastAPI)

Endpoints
- Health:
  - GET /health
  - GET / (backward compatibility)
- Users:
  - GET /users
  - POST /users
  - GET /users/{id}
  - PUT /users/{id}
  - DELETE /users/{id}
- Games:
  - GET /games
  - POST /games
  - GET /games/{id}
  - PUT /games/{id}
  - DELETE /games/{id}

Notes
- Data is stored in-memory as a placeholder. Replace with a real database in production.
- OpenAPI tags are defined for Health, Users, and Games.

How to Run
- The project is preconfigured to start via the existing entry at `carrom_backend/src/api/main.py`, which imports the fully configured app from `carrom_backend/app/main.py`.
- Swagger UI: http://localhost:3017/docs
- OpenAPI JSON: http://localhost:3017/openapi.json

Environment
- No required environment variables for this scaffold.
- See `carrom_backend/.env.example` for future reference.
