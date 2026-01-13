Mini AI Agent – FastAPI Backend (POC)

This project is a backend proof of concept for a simple AI agent built using FastAPI.
The service receives a natural language prompt, analyzes user intent, and routes the request to one of two internal tools:

🧮 Calculator Tool – evaluates math expressions
🧠 Memory Tool – stores and retrieves key–value data from a database

The goal of this POC is to demonstrate backend fundamentals such as API design, database interaction, and rule-based agent reasoning.

🚀 Features

Single agent brain endpoint (POST /agent/query)
Rule-based intent detection and routing
Calculator tool for basic math expressions
Memory tool with database persistence
SQLite database using SQLAlchemy
Request/response validation with Pydantic
Clean, modular code structure
Graceful error handling

🛠 Tech Stack

Python 3.10+
FastAPI
SQLAlchemy
SQLite (used instead of PostgreSQL for simplicity)
Pydantic
Uvicorn

📁 Project Structure

mini-ai-agent/
│
├── main.py               # FastAPI application entry point
├── agent/
│   ├── router.py         # Intent detection \& tool routing logic
│   ├── calculator.py    # Calculator tool
│   └── memory.py        # Memory tool│
├── db/
│   ├── database.py      # Database connection \& session
│   └── models.py        # SQLAlchemy models
│
├── schemas/
│   └── schemas.py       # Pydantic request/response models
│
├── requirements.txt
└── README.md

⚙️ Setup Instructions

1️⃣ Create Virtual Environment (Recommended)

python -m venv venv

Activate it:

Linux / macOS
source venv/bin/activate

Windows

venv\\Scripts\\activate

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Server

uvicorn main:app --reload

Server will start at:
http://127.0.0.1:8000

Swagger API documentation:
http://127.0.0.1:8000/docs

🔌 API Reference

POST /agent/query

This endpoint acts as the agent brain.
It analyzes the user prompt, determines intent, executes the appropriate tool, and returns a unified response.

Request Body
{
"prompt": "What is 10 plus 5?"
}

🧠 Agent Logic (How It Works)

Receive the user prompt
Analyze intent using simple rule-based logic:
Calculator → math-related prompts
Memory Save → prompts with “remember”, “save”
Memory Read → prompts with “what is my”, “recall”
Extract required entities from the prompt
Execute the selected tool
Return a structured JSON response

🧪 Example Queries

Calculator
{
"prompt": "What is 10 plus 5?"
}

Response

{
"original\_prompt": "What is 10 plus 5?",
"chosen\_tool": "calculator",
"tool\_input": "10 + 5",
"response": {
"result": 15
}
}

Save Memory
{
"prompt": "Remember my cat's name is Fluffy"
}

Response

{
"chosen\_tool": "memory\_save",
"response": {
"key": "cat's name",
"value": "Fluffy",
"status": "saved"
}
}

Retrieve Memory
{
"prompt": "What is my cat's name?"
}

Response

{
"chosen\_tool": "memory\_read",
"response": {
"key": "cat's name",
"value": "Fluffy"
}
}

❌ Error Handling

If the agent cannot match a prompt to any tool:

{
"error": "I do not have a tool for that."
}

🎯 Purpose of This POC

This project demonstrates:
FastAPI backend design
Database CRUD operations
Rule-based agent reasoning
Clean separation of concerns
Practical AI-agent-style architecture (without an LLM)

🔮 Possible Improvements

Replace rule-based routing with an LLM (LangChain / LangGraph)
Add authentication \& authorization
Add unit and integration tests
Support more tools (notes, search, weather, etc.)
Switch to PostgreSQL for production