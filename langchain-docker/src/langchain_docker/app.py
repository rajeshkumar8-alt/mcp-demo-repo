from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .chains import generate_response

app = FastAPI()


class ChatRequest(BaseModel):
    query: str | None = None


@app.get("/")
def greet():
    return {"message": "Hello, welcome to the chat API!"}


@app.get("/chat")
def chat_help():
    return {
        "message": "POST JSON to /chat with {'query': '...'}",
        "example": {"query": "hello"},
    }


@app.post("/chat")
async def chat(data: ChatRequest ):
    if  not data.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Provide JSON body like {'query': 'hello'} when calling POST /chat.",
        )

    response = generate_response(data.query)
    return {
            "response": response
        }
  




