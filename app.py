from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# System prompt defining assistant role
template = """
You are an AI Automation Blueprint Generator.
Your job is to design clear, step-by-step automation workflows
for small businesses using tools like Zapier, Make.com, CRMs, and email platforms.

Conversation:
{history}
Human: {input}
AI:
"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

llm = Ollama(model="llama3")

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

print("AI Automation Blueprint Generator")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = conversation.predict(input=user_input)
    print("\nAssistant:\n", response, "\n")