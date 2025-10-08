from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
import random

# Simulación de init_chat_model para que sea ejecutable
# En tu caso, usa tu import original: from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model


# Configuración del LLM (reemplaza con tu init_chat_model)
llm = init_chat_model("gemini-2.0-flash-001", temperature=0)
class State(MessagesState):
    customer_name: str
    my_age: int


def node_1(state: State):
    new_state: State = {}
    if state.get("customer_name") is None:
        new_state["customer_name"] = "John Doe"
    else:
        new_state["my_age"] = random.randint(20, 30)

    history = state["messages"]
    ai_message = llm.invoke(history)
    new_state["messages"] = [ai_message]
    return new_state

from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, 'node_1')
builder.add_edge('node_1', END)

agent = builder.compile()