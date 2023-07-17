import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]
modelo = "gpt-3.5-turbo"

with st.sidebar:
    st.title("Parâmetros do Modelo")
    temperatura=st.number_input("Temperatura (0 a 1)", min_value=0.0,max_value=1.0,value=0.5,step=0.1,format="%.1f")
    maxtokens=st.number_input("Máximo Númrero de Tokens (<500)", min_value=50,max_value=500,value=200,step=10)
    presencypenalty=st.number_input("Penalização por Presença (-2 a 2)", min_value=-2.0,max_value=2.0,value=0.0,step=0.1,format="%.1f")
    frequencypenalty=st.number_input("Penalizaçâo por Frequencia (-2 a 2)", min_value=-2.0,max_value=2.0,value=0.0,step=0.1,format="%.1f")
               
    
st.title("OpenAI Chatbot")
st.session_state["messages"] = [ ]
        
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como posso lhe ajudar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("O que gostaria de saber"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model=modelo,temperature=temperatura,max_tokens=maxtokens,messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
