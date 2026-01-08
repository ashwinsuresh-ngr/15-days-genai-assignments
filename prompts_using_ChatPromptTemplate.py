from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "What are 3 benefits of {technology} in {field}?")
    
])

messages = prompt.format_messages(
    technology="AI",
    field="healthcare"
)

for msg in messages:
    print(msg.content)