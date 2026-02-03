"""AI API routes."""
from fastapi import APIRouter, status

from src.ai.schemas import ChatRequest, ChatResponse
from src.ai.service import process_message

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    description="Send a message to the LLM via LangGraph",
    summary="Chat with LLM",
)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process a chat message through LangGraph workflow."""
    response = await process_message(request.message)
    return ChatResponse(response=response)
