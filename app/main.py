from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.middleware.index import log_requests
from app.middleware.cors import add_cors_middleware
from app.exception.index import exception_handler
from pydantic import BaseModel
from app.core.config import settings

print("App:", settings.app_name)
print("OpenAI key:", settings.openai_api_key)
print("Groq key:", settings.groq_api_key)

app = FastAPI()
app.middleware("http")(log_requests)
app.add_exception_handler(HTTPException, exception_handler)
app.add_exception_handler(StarletteHTTPException, exception_handler)
add_cors_middleware(app)

class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7
    
@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/health")
def health():
    return {"status": "healthy"}