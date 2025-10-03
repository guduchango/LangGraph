from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage

# Estado que hereda de MessagesState para tener historial automático
class State(MessagesState):
    contador_interacciones: int = 0


def chatbot_node(state: State):
    """
    Este nodo demuestra cómo trabajar con el historial de mensajes.
    MessagesState mantiene automáticamente una lista de mensajes en state["messages"]
    """
    
    # Acceder al historial completo
    historial = state["messages"]
    
    # Obtener el último mensaje del usuario
    ultimo_mensaje = historial[-1] if historial else None
    
    # Contar interacciones
    nuevo_contador = state.get("contador_interacciones", 0) + 1
    
    # Crear respuesta basada en el historial
    if nuevo_contador == 1:
        respuesta = AIMessage(content="¡Hola! Soy tu asistente. ¿En qué puedo ayudarte?")
    elif nuevo_contador == 2:
        respuesta = AIMessage(
            content=f"Veo que dijiste: '{ultimo_mensaje.content}'. ¿Algo más?"
        )
    else:
        num_mensajes = len(historial)
        respuesta = AIMessage(
            content=f"Llevamos {num_mensajes} mensajes en total. El historial se mantiene automáticamente."
        )
    
    # Retornar el nuevo mensaje (se agrega automáticamente al historial)
    return {
        "messages": [respuesta],
        "contador_interacciones": nuevo_contador
    }


# Construir el grafo
builder = StateGraph(State)
builder.add_node("chatbot", chatbot_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

agent = builder.compile()