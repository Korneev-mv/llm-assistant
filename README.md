# LLM Assistant — FastAPI + Ollama

Pet-проект: REST API на FastAPI с интеграцией локальной LLM через Ollama. Два эндпоинта: ответ на вопрос и суммаризация текста.

## Стек

- Python 3.12
- FastAPI
- Uvicorn
- OpenAI Python SDK (для работы с Ollama через OpenAI-совместимый API)
- Ollama (локальный запуск LLM)
- python-dotenv

## Функционал

- **GET /** — health-check
- **POST /ask** — принимает вопрос, возвращает ответ от LLM
- **POST /summarize** — принимает текст, возвращает краткое резюме
- Настройки (URL модели, имя модели) вынесены в .env
- Обработка ошибок LLM: если Ollama недоступен, сервер возвращает 500, а не падает
- Модель можно сменить одной строчкой в .env (llama3.2 → gemma2:9b)

## Запуск

### 1. Установить Ollama

Скачать с https://ollama.com/download и установить.

### 2. Скачать модель

ollama pull llama3.2

Или модель получше (если есть 16 ГБ ОЗУ):

ollama pull gemma2:9b

### 3. Клонировать репозиторий

```bash 
git clone https://github.com/Korneev-mv/llm-assistant.git
cd llm-assistant
```

### 4. Создать виртуальное окружение
```bash
python -m venv .venv
source .venv/bin/activate  (Linux/macOS)
.venv\Scripts\activate     (Windows)
```
### 5. Установить зависимости
```bash
pip install -r requirements.txt
```

### 6. Создать .env

```bash
OLLAMA_BASE_URL=http://localhost:11434/v1
MODEL_NAME=llama3.2
```

### 7. Запустить
```bash
uvicorn app.main:app --reload
```
http://localhost:8000/docs — Swagger-документация.

## Примеры запросов

### POST /ask

{
  "question": "Что такое FastAPI?"
}

Ответ:

{
  "answer": "FastAPI — это современный веб-фреймворк для Python..."
}

### POST /summarize

{
  "text": "Длинный текст для суммаризации..."
}

Ответ:

{
  "summary": "Краткое резюме текста..."
}

## Как это работает

FastAPI-сервер принимает запрос и через OpenAI Python SDK обращается к локальному серверу Ollama по адресу http://localhost:11434/v1. Ollama запускает скачанную модель и возвращает ответ. Формат API совместим с OpenAI, поэтому в коде используется стандартный клиент openai.
