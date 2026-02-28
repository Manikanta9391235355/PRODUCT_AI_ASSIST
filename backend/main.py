from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from products import products
from llm_service import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
def get_products(category: str = None):
    if category:
        return [p for p in products if p["category"] == category]
    return products

@app.post("/api/ask")
def ask_products(data: dict):
    try:
        result = ask_llm(data["query"])
        matched = [p for p in products if p["id"] in result["productIds"]]
        return {
            "products": matched,
            "summary": result["summary"]
        }
    except Exception:
        raise HTTPException(status_code=502, detail="LLM service unavailable")