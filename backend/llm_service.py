import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from products import products

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(user_query: str):
    product_context = "\n".join(
        [f'{p["id"]}. {p["name"]} - {p["category"]} - ${p["price"]} - {p["description"]}'
         for p in products]
    )

    prompt = f"""
You are a product assistant.

User query:
"{user_query}"

Available products:
{product_context}

Return ONLY valid JSON:
{{
    "productIds": [list of matching product IDs],
    "summary": "Short explanation"
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    content = response.choices[0].message.content
    return json.loads(content)