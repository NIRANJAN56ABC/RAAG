from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_answer(query: str, context: str):
    prompt = f"""
You are an AI assistant.

Use ONLY  context below to answer.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content