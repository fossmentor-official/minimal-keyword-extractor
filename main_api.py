from fastapi import FastAPI
from pydantic import BaseModel
from extractor import extract_keywords

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/extract")
def extract(input: TextInput):
    keywords = extract_keywords(input.text)
    return {"keywords": keywords}