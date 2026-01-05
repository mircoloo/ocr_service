from pypdf import PdfReader
from pypdf.errors import PdfReadError


def is_file_valid_pdf(file_path) -> bool:
    try:
        PdfReader(file_path)
        return True
    except PdfReadError:
        return False

