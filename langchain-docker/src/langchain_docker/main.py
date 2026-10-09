from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ChatRequest(BaseModel):
    query: str


@app.get("/")
def greet():
    return {"message": "Hello, welcome to the chat API!"}


@app.post("/chat")
async def chat(data: ChatRequest):
    return {"response": f"You asked: {data.query}"}


