from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Question(BaseModel):
    question: str

# API Endpoint
@app.post("/ask")
def ask(question: Question):

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
       messages=[
    {
        "role": "system",
        "content": "You are AI Study Buddy. Give short, simple answers in 5-8 lines that are easy for students to understand."
    },
    {
        "role": "user",
        "content": question.question
    }
]
    )

    answer = completion.choices[0].message.content

    return {
        "answer": answer
    }