from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["country", "informations"],
    template="who are the 3 previous president of {country} and their {informations} ?"
)

formatted_prompt = prompt.format(
    country="India",
    informations="Ruling years "
)

print(formatted_prompt)