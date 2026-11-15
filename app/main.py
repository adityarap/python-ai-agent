
from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run_agent

app = FastAPI(title="Python AI Agent API")


class AgentRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/agent/run")
def execute_agent(request: AgentRequest):
    response = run_agent(request.question)

    return {
        "question": request.question,
        "response": response
    }
