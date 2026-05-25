from fastapi import APIRouter
from app.services.retriever import retrieve
from app.services.generator import generate_answer

router = APIRouter()

@router.get("/query")
def query(q: str):
    context = retrieve(q, k=3)
    answer = generate_answer(q, context)

    return {
        "question": q,
        "context": context,
        "answer": answer
    }