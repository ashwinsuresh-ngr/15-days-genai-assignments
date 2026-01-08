import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


api_key = os.getenv("GEMINI_API_KEY")


template_str = "who are the 3 previous president of {country} and their {informations}?"
prompt = PromptTemplate(
    input_variables=["country", "informations"],
    template=template_str
)

formatted_prompt = prompt.format(country="India", informations="Ruling years")
print("Formatted Prompt:\n", formatted_prompt)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="AIzaSyCxDoPGLovO2u8YA2GjyHA03NumWY1eK78"
)

result = model.invoke(formatted_prompt)

print("\nAI Response:\n", result.content)