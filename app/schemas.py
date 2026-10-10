from pydantic import BaseModel


class AskRequest(BaseModel):
    """Тело запроса для /ask"""
    question: str


class AskResponse(BaseModel):
    """Ответ для /ask"""
    answer: str


class SummarizeRequest(BaseModel):
    """Тело запроса для /summarize"""
    text: str


class SummarizeResponse(BaseModel):
    """Ответ для /summarize"""
    summary: str