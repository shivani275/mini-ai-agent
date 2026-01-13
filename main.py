from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import AgentRequest, AgentResponse
from router import route_prompt
from tools import tool_calculate, tool_save_memory, tool_get_memory

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Mini Agent")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/agent/query", response_model=AgentResponse)
def agent_query(req: AgentRequest, db: Session = Depends(get_db)):
    tool, key, value = route_prompt(req.prompt)

    if tool == "calculator":
        result = tool_calculate(key)
    elif tool == "memory_save":
        result = tool_save_memory(db, key, value)
    elif tool == "memory_read":
        result = tool_get_memory(db, key)
    else:
        return {
            "original_prompt": req.prompt,
            "chosen_tool": "none",
            "tool_input": "",
            "response": {"error": "I do not have a tool for that."}
        }
    return {
        "original_prompt": req.prompt,
        "chosen_tool": tool,
        "tool_input": key,
        "response": result
    }
