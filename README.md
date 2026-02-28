# 🛍 Product AI Assist  
Mini Full-Stack Product Discovery App with LLM Integration  

## 📌 Overview

This project is a mini product discovery experience built as part of a Full-Stack Developer assessment.  

It includes:

- ✅ FastAPI backend with REST endpoints  
- ✅ React frontend (Vite)  
- ✅ LLM-powered natural language search  
- ✅ Structured JSON parsing from LLM  
- ✅ Error handling and clean architecture  

The application allows users to:
- Browse products
- Ask natural language questions (e.g., "Show me budget laptops")
- Receive AI-powered filtered results + summary

---

## 🏗 Tech Stack

### Backend
- Python
- FastAPI
- OpenAI API (LLM integration)
- Uvicorn
- python-dotenv

### Frontend
- React (Vite)
- Fetch API
- useState & useEffect hooks

---

## 📂 Project Structure

product-ai-assist/
│
├── backend/
│ ├── main.py
│ ├── products.py
│ ├── llm_service.py
│ ├── requirements.txt
│ └── .env (not committed)
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ └── main.jsx
│ ├── package.json
│ └── index.html
│
└── README.md
1️⃣ How to Run the Project
🔹 Backend Setup (FastAPI)
Step 1: Navigate to backend folder
cd backend
Step 2: Create virtual environment
python -m venv venv
Step 3: Activate virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
Step 4: Install dependencies
pip install -r requirements.txt
Step 5: Set environment variable

Create a .env file inside backend/:

OPENAI_API_KEY=your_api_key_here

⚠️ Do not commit .env file.

Step 6: Run backend server
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
🔹 Frontend Setup (React + Vite)
Step 1: Navigate to frontend folder
cd frontend
Step 2: Install dependencies
npm install
Step 3: Run frontend
npm run dev

Frontend runs at:

http://localhost:5173
2️⃣ What’s Implemented
✅ Backend
Product Catalog

5–8 mock products stored in memory

Each product includes:

id

name

category

price

description

tags

REST Endpoints
🔹 GET /api/products

Returns all products

Supports optional filtering by category

Example:

/api/products
/api/products?category=laptop
🔹 POST /api/ask

Accepts natural language query:

{
  "query": "Show me budget laptops"
}
LLM Used

OpenAI-compatible API (gpt-4o-mini)

API key loaded securely from environment variables

🤖 AI “Ask” Flow

User types a natural language query in frontend.

Frontend sends POST request to /api/ask.

Backend:

Builds prompt including:

User query

Product catalog context

Calls LLM.

Instructs model to return structured JSON:

{
  "productIds": [...],
  "summary": "Short explanation"
}

Backend parses JSON safely.

Returns:

{
  "products": [...],
  "summary": "..."
}

Frontend displays:

Filtered product list

AI-generated summary

✅ Frontend

Product list display

Natural language "Ask" input

Loading state handling

Error handling

Reusable ProductCard component

API integration using fetch

State management using useState and useEffect

3️⃣ Time Spent

Approximately ~3 hours

Backend + LLM integration: ~1.5 hours

Frontend + API integration: ~1.25 hours

Testing + README + cleanup: ~30 minutes

