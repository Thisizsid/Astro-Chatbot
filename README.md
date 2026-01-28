# Astro-Chatbot

A FastAPI + OpenAI chatbot API that **only answers astrology-related questions**.  
It supports:
- English
- Nepali (देवनागरी)
- Nepali written in Roman letters (e.g., “ma janmeko din… kundali bhannus”)

If a user asks anything outside astrology, the API refuses.

---

## Features
- Astrology-only responses (strict scope)
- Nepali + Romanized Nepali support (replies in the same style as the user)
- Topic gate using an LLM classifier to block non-astrology queries
- Simple JSON API endpoint: `POST /chat`

---

## Tech Stack
- Python
- FastAPI
- Uvicorn
- OpenAI API (`gpt-4o-mini`)

---

## Setup

### 1) Clone
```bash
git clone https://github.com/Thisizsid/Astro-Chatbot.git
cd Astro-Chatbot


2) Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

3) Install dependencies
pip install fastapi uvicorn openai python-dotenv

4) Add your API key
Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here


Run the server
uvicorn main:app --reload --port 8000

Open docs:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
API Usage
Endpoint
POST /chat

Request body
{
  "message": "your question",
  "history": [
    {"role": "user", "content": "previous message"},
    {"role": "assistant", "content": "previous reply"}
  ]
}

curl examples
English
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"What does Aries rising mean?"}'

Nepali (देवनागरी)
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"मेष लग्नको अर्थ के हो?"}'

Nepali (Romanized)
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"ma janmeko din 2058-01-12 ho, time 7:15 am, janma sthan pokhara. yo hisab le mero kundali bhannus"}'

Non-astrology (should refuse)
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"Write a Python function to sort a list"}'

