from fastapi import FastAPI, UploadFile, File
from app.ocr_service import extract_text_async  # funzione sincrona ora
import uuid, os
from app.utils import is_file_valid_pdf
from pathlib import Path

app = FastAPI()

TEMP_DIR = "/tmp/uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/extract_text")
async def extract_text_endpoint(file: UploadFile = File(...)):
    if not is_file_valid_pdf(Path().cwd() / "app" / file.filename):
        return {"error": "Invalid PDF file"}
    file_id = f"{uuid.uuid4()}.pdf"
    path = os.path.join(TEMP_DIR, file_id)
    with open(path, "wb") as f:
        f.write(await file.read())
    text = await extract_text_async(path)
    os.remove(path)
    return {"text": text}

