"""LangGraph service for AI workflows."""
from typing import TypedDict

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph

from src.ai.config import ai_settings


class GraphState(TypedDict):
    """State passed through the LangGraph workflow."""
    message: str
    response: str


async def call_llm(state: GraphState) -> GraphState:
    """Node that calls OpenAI LLM with user message."""
    llm = ChatOpenAI(api_key=ai_settings.OPENAI_API_KEY, model="gpt-4o-mini")
    
    messages = [HumanMessage(content=state["message"])]
    response = await llm.ainvoke(messages)
    
    return {
        "message": state["message"],
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
    """Process a user message through the LangGraph workflow."""
    initial_state: GraphState = {
        "message": message,
        "response": "",
    }
    
    result = await graph.ainvoke(initial_state)
    return result["response"]
