"""LangGraph service for AI workflows."""
from typing import Any, TypedDict
from uuid import UUID, uuid4

from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph

from src.ai.config import ai_settings


class GraphState(TypedDict):
    """State passed through the LangGraph workflow."""
    messages: list[dict[str, str]]  # Conversation history
    response: str


class ThreadRepository:
    """In-memory thread repository for conversation history."""
    
    def __init__(self) -> None:
        """Initialize with empty storage."""
        self._threads: dict[UUID, list[dict[str, str]]] = {}
    
    async def create_thread(self) -> UUID:
        """Create a new conversation thread."""
        thread_id = uuid4()
        self._threads[thread_id] = []
        return thread_id
    
    async def get_thread_history(self, thread_id: UUID) -> list[dict[str, str]]:
        """Get conversation history for a thread."""
        return self._threads.get(thread_id, [])
    
    async def add_message(self, thread_id: UUID, role: str, content: str) -> None:
        """Add a message to thread history."""
        if thread_id not in self._threads:
            self._threads[thread_id] = []
        
        self._threads[thread_id].append({"role": role, "content": content})
    
    async def thread_exists(self, thread_id: UUID) -> bool:
        """Check if thread exists."""
        return thread_id in self._threads


# Singleton thread repository instance
thread_repository = ThreadRepository()


async def call_llm(state: GraphState) -> GraphState:
    """Node that calls OpenAI LLM with conversation history."""
    llm = ChatOpenAI(api_key=ai_settings.OPENAI_API_KEY, model="gpt-4o-mini")
    
    # Convert history to LangChain messages
    langchain_messages = []
    for msg in state["messages"]:
        if msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(AIMessage(content=msg["content"]))
    
    response = await llm.ainvoke(langchain_messages)
    
    return {
        "messages": state["messages"],
        "response": response.content,
    }


def create_graph() -> StateGraph:
    """Create and return the LangGraph workflow."""
    workflow = StateGraph(GraphState)
    
    # Add node
    workflow.add_node("call_llm", call_llm)
    
    # Set entry point
    workflow.set_entry_point("call_llm")
    
    # Set exit point
    workflow.add_edge("call_llm", END)
    
    # Compile graph
    return workflow.compile()


# Singleton graph instance
graph = create_graph()


async def process_message(message: str) -> str:
    """Process a user message through the LangGraph workflow (stateless)."""
    initial_state: GraphState = {
        "messages": [{"role": "user", "content": message}],
        "response": "",
    }
    
    result = await graph.ainvoke(initial_state)
    return result["response"]


async def process_thread_message(thread_id: UUID, message: str) -> str:
    """Process a message in a thread with conversation history."""
    # Get existing history
    history = await thread_repository.get_thread_history(thread_id)
    
    # Add user message to history
    await thread_repository.add_message(thread_id, "user", message)
    
    # Prepare state with full history
    initial_state: GraphState = {
        "messages": history + [{"role": "user", "content": message}],
        "response": "",
    }
    
    # Call graph
    result = await graph.ainvoke(initial_state)
    ai_response = result["response"]
    
    # Add AI response to history
    await thread_repository.add_message(thread_id, "assistant", ai_response)
    
    return ai_response
