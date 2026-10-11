# Python Skeleton Fast API

A FastAPI skeleton project with middleware, CORS, exception handling, and configuration management. Built for AI projects with frontend + backend architecture.

## Project Structure

```
AI_Assistant/
├── app/
│   ├── core/
│   │   └── config.py          # Pydantic settings from .env
│   ├── exception/
│   │   └── index.py           # Global exception handler
│   ├── middleware/
│   │   ├── index.py           # HTTP request logging middleware
│   │   └── cors.py            # CORS middleware setup
│   └── main.py                # FastAPI app entry point
├── .env                       # Environment variables (never commit)
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Setup

```bash
# Install dependencies
uv sync

# Run the server
uv run uvicorn app.main:app --reload
```

## Configuration

Create a `.env` file at the project root:

```env
APP_NAME=AI Assistant
APP_ENV=development
APP_PORT=8000

OPENAI_API_KEY=your-key
GROQ_API_KEY=your-key
```

**Never commit `.env`** — it's already in `.gitignore`.

Settings are managed centrally in `app/core/config.py` using Pydantic Settings:

```python
from app.core.config import settings

print(settings.app_name)
print(settings.openai_api_key)
```

### Priority order (highest to lowest)

1. OS environment variables
2. `.env` file
3. Class default values

## Middleware

### Request Logging (`app/middleware/index.py`)

Logs each request including method, URL, and server port:

```python
async def log_requests(request, call_next):
    host, port = request.scope.get("server", ("", 0))
    print(f"Request: {request.method} {request.url}")
    print(f"Server: {host}:{port}")
    response = await call_next(request)
    return response
```

Registered in `main.py`:

```python
app.middleware("http")(log_requests)
```

### CORS (`app/middleware/cors.py`)

Allows your React frontend (port 5173) to call the FastAPI backend (port 8000):

```python
def add_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
```

**CORS is a browser security mechanism** — it does not replace authentication or authorization. Tools like Postman and curl are not affected by CORS.

## Exception Handling (`app/exception/index.py`)

Custom handler that produces consistent JSON responses:

```python
async def exception_handler(request: Request, exc: HTTPException):
    print(f"Exception handled: {exc.status_code} - {exc.detail} for {request.method} {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
```

Registered for both exception types:

```python
app.add_exception_handler(HTTPException, exception_handler)
app.add_exception_handler(StarletteHTTPException, exception_handler)
```

### Important distinction

- `fastapi.HTTPException` — catches exceptions **you raise** in route code
- `starlette.exceptions.HTTPException` — catches FastAPI's **built-in** errors (404, 405, etc.)

Both are needed to cover all cases.

## Endpoints

| Method | Path        | Description        |
|--------|-------------|--------------------|
| GET    | `/`         | Home               |
| GET    | `/health`   | Health check       |

## Adding Dependencies

Use `uv add` (never edit `pyproject.toml` manually):

```bash
# Production dependencies
uv add fastapi uvicorn pydantic httpx openai

# Development dependencies
uv add --dev pytest ruff
```

For AI/LLM projects:

```bash
uv add openai tiktoken
uv add chromadb sentence-transformers  # RAG / vector DB
uv add numpy pandas                    # Data processing
```

## Architecture

```
React (frontend)
       ↓ HTTP/WebSocket
CORS Middleware
       ↓
Logging Middleware
       ↓
FastAPI Router
       ↓
Service Layer
       ↓
AI / Database
       ↓
Response
```

## Logging

Replace `print()` with proper logging as the project grows:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Request received")
logger.error("Something went wrong")
```

## Environment Variables

Use Pydantic Settings instead of `os.getenv()` everywhere. This gives you:

- Centralized configuration
- Type validation
- Automatic `.env` loading
- Support for multiple environments (`.env.development`, `.env.production`)

## Security Notes

- Never commit secrets to source code
- Use environment variables for API keys
- Set appropriate CORS origins for production
- CORS is not authentication
