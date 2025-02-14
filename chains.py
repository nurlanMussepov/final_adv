from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = Ollama(model="llama2")

swear_words = ["not good", "bad person", "bad grade"]  

def filter_swear_words(text):
    for word in swear_words:
        if word in text.lower():
            return True, "This message contains inappropriate content."
    return False, text

def create_chain(memory):
    prompt = PromptTemplate(
        input_variables=["input", "history"],
        template="You are a helpful AI assistant. Conversation history: {history}\nUser: {input}\nAI:"
    )
    return LLMChain(llm=llm, prompt=prompt, memory=memory)
