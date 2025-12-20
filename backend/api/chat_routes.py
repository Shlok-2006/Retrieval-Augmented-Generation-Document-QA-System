from fastapi import APIRouter
from pydantic import BaseModel
from backend.rag.retriever import retrieve
from backend.rag.generator import generate_answer

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/chat")
def chat(query: Query):
    contexts = retrieve(query.question)
    answer = generate_answer(query.question, contexts)

    return {
        "answer": answer,
        "sources": contexts
    }
