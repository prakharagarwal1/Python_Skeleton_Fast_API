from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.middleware.index import log_requests
from app.middleware.cors import add_cors_middleware
from app.exception.index import exception_handler
# from app.core.config import settings
# from app.core.logging import logger
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router
from app.api.routes.default import router as default
from contextlib import asynccontextmanager
from app.core.database import engine
from app.core.init_db import init_db
from app.api.routes.users import router as users_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await engine.dispose()



# logger.info("App:", settings.app_name)
# logger.info("OpenAI key:", settings.openai_api_key)
# logger.info("Groq key:", settings.groq_api_key)
# logger.info("Application started")
# logger.warning("Something looks unusual")
# logger.error("Something failed")
app = FastAPI(lifespan=lifespan)
app.middleware("http")(log_requests)
app.add_exception_handler(HTTPException, exception_handler)
app.add_exception_handler(StarletteHTTPException, exception_handler)
add_cors_middleware(app)

app.include_router(health_router,prefix="/api/v1")
app.include_router(chat_router,prefix="/api/v1")
app.include_router(default,prefix="/api/v1")
app.include_router( users_router, prefix="/api/v1")


