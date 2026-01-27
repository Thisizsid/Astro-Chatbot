
A FastAPI + OpenAI API backend that **only responds to astrology-related queries**.  
If a request is not about astrology, the API returns a refusal message.

Supports:
- English
- Nepali (देवनागरी)
- Nepali written in Roman letters


## Endpoint

### `POST /chat`

**Request JSON**
```json
{
  "message": "string",
  "history": [
    {"role": "user", "content": "string"},
    {"role": "assistant", "content": "string"}
  ]
}

