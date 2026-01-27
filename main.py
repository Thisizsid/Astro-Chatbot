import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from systemprompt import MAIN_SYSTEM_PROMPT
from classifierprompt import MAIN_CLASSIFIER_PROMPT

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

app = FastAPI()

MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = MAIN_SYSTEM_PROMPT

CLASSIFIER_PROMPT = MAIN_CLASSIFIER_PROMPT

class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []  

def classify_astrology(text: str) -> bool:
    r = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": CLASSIFIER_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.0,
    )
    label = (r.output_text or "").strip()
    return label == "ASTROLOGY"


@app.get("/")
def root():
    return {"status": "ok", "hint": "POST /chat or open /docs"}

@app.post("/chat")
def chat(req: ChatRequest):
    if not classify_astrology(req.message):
        return {
            "reply": (
                "I can only help with astrology-related questions. "
                "Try asking about your rashi/zodiac, kundali (birth chart), or current transits—"
                "include birth date, exact time, and birthplace if you want a kundali-style reading."
            )
        }

    # Main response
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    for m in req.history:
        if m.get("role") in ("user", "assistant") and isinstance(m.get("content"), str):
            msgs.append({"role": m["role"], "content": m["content"]})
    msgs.append({"role": "user", "content": req.message})

    r = client.responses.create(
        model=MODEL,
        input=msgs,
        temperature=0.2,
    )

    reply = r.output_text or ""

    # Optional post-check (extra strict)
    if not classify_astrology(reply):
        reply = "I can only help with astrology-related questions."

    return {"reply": reply}