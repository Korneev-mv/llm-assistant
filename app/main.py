from fastapi import FastAPI, HTTPException

from app.schemas import (
    AskRequest,
    AskResponse,
    SummarizeRequest,
    SummarizeResponse,
)
from app.services.llm_service import ask, summarize

app = FastAPI(
    title="LLM Assistant",
    description="Pet-проект: FastAPI + локальная LLM через Ollama",
    version="0.1.0",
)


@app.get("/")
def root():
    """Проверка, что сервер жив."""
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest) -> AskResponse:
    """Принимает вопрос, возвращает ответ от LLM."""
    try:
        answer = ask(request.question)
        return AskResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_endpoint(request: SummarizeRequest) -> SummarizeResponse:
    """Принимает текст, возвращает краткое резюме."""
    try:
        summary = summarize(request.text)
        return SummarizeResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")