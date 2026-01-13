import re
from sqlalchemy.orm import Session
from database import Memory

def tool_save_memory(db: Session, key: str, value: str) -> dict:
    record = db.query(Memory).filter(Memory.key == key).first()
    if record:
        record.value = value
    else:
        record = Memory(key=key, value=value)
        db.add(record)

    db.commit()
    return {"key": key, "value": value}

def tool_get_memory(db: Session, key: str) -> dict:
    record = db.query(Memory).filter(Memory.key == key).first()
    if not record:
        return {"error": "Key not found"}
    return {"key": key, "value": record.value}

def tool_calculate(expression: str) -> dict:
    safe_expr = re.sub(r"[^0-9+\-*/(). ]", "", expression)
    try:
        result = eval(safe_expr)
        return {"result": result}
    except Exception:
        return {"error": "Invalid expression"}
