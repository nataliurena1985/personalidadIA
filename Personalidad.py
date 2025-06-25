import streamlit as st
import openai

st.set_page_config(page_title="Chatbot Colombiano 🇨🇴", page_icon="🤖")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Instrucción inicial con tono colombiano y amigable
sistema = {
    "role": "system",
    "content": "Eres un asistente virtual muy amable, con acento y expresiones típicas de Colombia. "
               "Respondes con calidez, usando frases como 'parce', 'qué nota', 'bacano' y siempre das buena vibra. "
               "Tu tono es cercano, relajado y simpático, como un amigo colombiano que quiere ayudar."
}

# Inicializar historial
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [sistema]

# Mostrar historial
for m in st.session_state.mensajes[1:]:
    st.chat_message(m["role"]).write(m["content"])

# Entrada del usuario
entrada = st.chat_input("Escribe tu mensaje, parce...")

if entrada:
    st.session_state.mensajes.append({"role": "user", "content": entrada})
    st.chat_message("user").write(entrada)

    respuesta = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=st.session_state.mensajes,
        temperature=0.8,
        max_tokens=600
    )

    contenido = respuesta.choices[0].message.content
    st.chat_message("assistant").write(contenido)
    st.session_state.mensajes.append({"role": "assistant", "content": contenido})