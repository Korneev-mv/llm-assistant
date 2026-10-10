from openai import OpenAI

from app.config import settings

client = OpenAI(
    base_url=settings.OLLAMA_BASE_URL,
    api_key="ollama",
)


def ask(question: str) -> str:
    """Отправляет вопрос в LLM и возвращает ответ."""
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "user", "content": question}
        ],
    )
    return response.choices[0].message.content


def summarize(text: str) -> str:
    """Делает краткое резюме текста через LLM."""
    prompt = f"Сделай краткое резюме следующего текста на русском языке:\n\n{text}"
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content