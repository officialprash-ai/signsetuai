from fastapi import FastAPI
from pydantic import BaseModel
from app.isl_converter import convert_to_isl
from app.token_mapper import map_to_tokens

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "SignSetu AI Backend Running 🚀"}

@app.post("/process")
def process_text(data: InputText):
    original = data.text
    isl_text = convert_to_isl(original)
    tokens = map_to_tokens(isl_text)

    return {
        "original": original,
        "isl": isl_text,
        "tokens": tokens
    }