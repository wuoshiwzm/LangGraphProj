"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent
from langgraph.runtime import Runtime
from typing_extensions import TypedDict

from env_utils import BAILIAN_API_KEY, BAILIAN_URL, CLOSEAI_API_KEY, CLOSEAI_BASE_URL
from src.agent.tools.tool_demos import calc


class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    my_configurable_param: str


@dataclass
class State:
    """Input state for the agent.

    Defines the initial structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    """

    changeme: str = "example"


async def call_model(state: State, runtime: Runtime[Context]) -> Dict[str, Any]:
    """Process input and returns output.

    Can use runtime context to alter behavior.
    """
    return {
        "changeme": "output from call_model. "
                    f"Configured with {(runtime.context or {}).get('my_configurable_param')}"
    }


# Define the graph
graph1 = (
    StateGraph(State, context_schema=Context)
    .add_node(call_model)
    .add_edge("__start__", "call_model")
    .compile(name="New Graph")
)

llm = ChatOpenAI(
    model='gpt-4o-mini',
    # model='qwen3-8b',
    temperature=0.8,
    api_key=CLOSEAI_API_KEY,
    base_url=CLOSEAI_BASE_URL,
    # extra_body={"enable_thinking": False},
    # extra_body={'chat_template_kwargs': {'enable_thinking': False}},
)

def get_weather(city:str) -> str:

    """get weather of city"""
    return f'always sunny in {city}'

graph = create_react_agent(
    llm,
    tools=[get_weather, calc],
    prompt='You are a helpful assistant'
)