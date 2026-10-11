from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response_msg: str
    response_temp: str