import streamlit as st
from chains import create_chain, filter_swear_words
from memory import initialize_memory, save_to_memory, load_memory
from telegram_bot import send_telegram_notification
import asyncio

memory = initialize_memory()

chain = create_chain(memory)

st.title("Advanced LLM Application")
st.write("This app uses Ollama, LangChain, and Streamlit to provide a conversational AI with advanced features.")

user_input = st.text_input("Enter your query:")

if user_input:
    has_swear_word, filtered_input = filter_swear_words(user_input)
    
    if has_swear_word:
        asyncio.run(send_telegram_notification(f"Swear word detected in query: {user_input}"))
        st.write("Response: This message contains inappropriate content.")
    else:
        response = chain.run(input=filtered_input)
        
        save_to_memory(memory, user_input, response)
        
        st.write("Response:", response)
