from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore
import os
app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=os.getenv("GROQ_API_KEY"))
    prompt = [{"role": "user", "content": "Come up with a new business idea for AI Agents"}]
    response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=prompt)
    return response.choices[0].message.content