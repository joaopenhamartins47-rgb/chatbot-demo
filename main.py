#Titulo
#Input do chat
#A cada mensagem que o usuario foi enviar:
    #Mostrar a mensagem que o usuario enviou
    #Pegar a pergunta e mandar pra IA
    #Exibir a resposta da IA na tela

# Streamlit -> Criacao do frontend e do backend
# IA: OpenAI

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
modelo_ia = OpenAI(api_key=api_key)

st.title("Chatbot com IA simples")

if not "contexto" in st.session_state: #Analise pelos cookies do usuario
    st.session_state["contexto"] = []

text_user = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["contexto"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if text_user:
    st.chat_message("user").write(text_user)
    # Posso colocar o nome, user ou assistant
    mensagem_usuario = {"role": "user", "content": text_user}
    st.session_state["contexto"].append(mensagem_usuario)

    # Resposta da ia retorna muita coisa alem do texto, por isso outra variavel pra filtragem da resposta
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["contexto"], model="gpt-4o")
    texto_resposta_ia = resposta_ia.choices[0].message.content
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.chat_message("assistant").write(texto_resposta_ia)
    st.session_state["contexto"].append(mensagem_ia)




