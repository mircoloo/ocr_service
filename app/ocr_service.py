import fitz 
import asyncio

def extract_text(file_path):
    doc = fitz.open(file_path)
    all_text = []
    for page_num, page in enumerate(doc):
        text = page.get_text()  # estrae solo il testo esistente
        all_text.append(text)

    return "\n".join(all_text)


async def extract_text_async(file_path):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, extract_text, file_path)
