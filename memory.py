from langchain.memory import ConversationBufferMemory

def initialize_memory():
    return ConversationBufferMemory()

def save_to_memory(memory, user_input, ai_response):
    memory.save_context({"input": user_input}, {"output": ai_response})

def load_memory(memory):
    return memory.load_memory_variables({})
