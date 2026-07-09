#Titulo
#Input do chat
#A cada mensagem que o usuario foi enviar:
    #Mostrar a mensagem que o usuario enviou
    #Pegar a pergunta e mandar pra IA
    #Exibir a resposta da IA na tela

# Streamlit -> Criacao do frontend e do backend
# IA: OpenAI

import streamlit as st

st.title("Chatbot com IA simples")

text_user = st.chat_input("Digite sua mensagem")

if text_user:
    print(text_user)


