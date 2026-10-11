from fastapi import APIRouter
from app.schemas.chat import ChatRequest,ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/chat")
async def chat(request: ChatRequest):
    # return {
    #     "response": f"You said: {request.message}"
    # }
    response = await chat_service.chat(
        request.message
    )

    return ChatResponse(
        response_msg=response,
        response_temp=str(2.5),
        model="demo-model"
    )