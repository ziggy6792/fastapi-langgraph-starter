"""AI API routes."""
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.ai.dependencies import valid_thread_id
from src.ai.schemas import (
    ChatRequest,
    ChatResponse,
    ThreadChatRequest,
    ThreadCreateResponse,
)
from src.ai.service import process_message, process_thread_message, thread_repository

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    description="Send a message to the LLM via LangGraph (stateless)",
    summary="Chat with LLM",
)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process a chat message through LangGraph workflow (no history)."""
    response = await process_message(request.message)
    return ChatResponse(response=response)


@router.post(
    "/threads",
    response_model=ThreadCreateResponse,
    status_code=status.HTTP_201_CREATED,
    description="Create a new conversation thread",
    summary="Create Thread",
)
async def create_thread() -> ThreadCreateResponse:
    """Create a new conversation thread."""
    thread_id = await thread_repository.create_thread()
    return ThreadCreateResponse(threadId=thread_id)


@router.post(
    "/threads/{thread_id}/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    description="Send a message to a conversation thread (maintains history)",
    summary="Chat with Thread",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Thread not found"},
    },
)
async def chat_with_thread(
    thread_id: UUID = Depends(valid_thread_id),
    request: ThreadChatRequest = ...,
) -> ChatResponse:
    """Process a message in a thread with conversation history."""
    response = await process_thread_message(thread_id, request.message)
    return ChatResponse(response=response)
