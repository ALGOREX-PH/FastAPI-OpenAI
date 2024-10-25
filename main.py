from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API key


# Define a request body model
class ChatRequest(BaseModel):
    api_key: str
    message: str

# Define a route for the chatbot
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        openai.api_key = request.api_key
        # Call OpenAI API to get the response
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use the appropriate model name
            messages=[{"role": "user", "content": request.message}],
            max_tokens=150,
            temperature=0.7
        )
        answer = response.choices[0].message["content"]
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the OpenAI FastAPI app!"}