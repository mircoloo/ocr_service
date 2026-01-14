from fastapi import FastAPI, UploadFile, File
from app.ocr_service import extract_text_async 
import uuid, os
from app.utils import is_file_valid_pdf
from pathlib import Path

app = FastAPI()

TEMP_DIR = Path("/tmp/uploads")
TEMP_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/extract_text")
async def extract_text_endpoint(file: UploadFile = File(...)):
    
    file_id = f"{uuid.uuid4()}.pdf"
    path = TEMP_DIR / file_id
    
    with open(path, "wb") as f:
        f.write(await file.read())
    
    if not is_file_valid_pdf(path):
        return {"error": "Invalid PDF file"}
    
    text = await extract_text_async(path)
    os.remove(path)
    return {"data": text}

