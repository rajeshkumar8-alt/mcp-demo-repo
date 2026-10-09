import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

parser=StrOutputParser()

api_key = os.getenv("DIAL_API_KEY", "dial-bqq96zju18wzvc0em9phhj6bsac")

llm = AzureChatOpenAI(
    api_key=api_key,
    azure_endpoint="https://ai-proxy.lab.epam.com",
    azure_deployment="gpt-5.6-terra-2026-07-09",  
    api_version="2025-04-01-preview",           
    default_headers={"Api-Key": api_key},        
)

prompt= PromptTemplate.from_template(

    """
you are a helpful assistant. Answer the following query based on the content that user will refer to you with greet HI/Hello Dear:
{query}


"""
)

chain= prompt | llm | parser

def generate_response(query: str) -> str:
    return chain.invoke({"query": query})