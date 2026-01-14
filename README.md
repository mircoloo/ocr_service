# OCR Service API

## Overview

This project provides an OCR (Optical Character Recognition) service implemented using **FastAPI**. The service exposes a single HTTP endpoint that accepts a PDF document as input and returns the extracted text. The application is designed to be run either directly with **Uvicorn** or as a **Docker container**.

The service validates uploaded files to ensure they are valid PDF documents before processing and is suitable for deployment as an online API.

---

## API Endpoint

### `POST /extract_text`

Extracts text from a PDF file.

**Request**

* Content-Type: `multipart/form-data`
* Form field:

  * `file`: PDF file to be processed

**Response (Success)**

```json
{
  "text": "{Extracted text content}"
}
```

**Response (Error)**

```json
{
  "error": "Invalid PDF file"
}
```

---

## Project Structure (Example)

```
.
├── app/
│   ├── main.py
│   ├── ocr_service.py
│   └── utils.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.10 or later
* pip
* (Optional) Docker

---

## Installation (Local Execution)

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application with Uvicorn

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```
http://localhost:8000
```

Interactive API documentation:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## Docker Deployment

### Dockerfile

The project includes a `Dockerfile` that builds a production-ready container image for the OCR service.

### Build the Docker image

```bash
docker build -t ocr-service .
```

### Run the Docker container

```bash
docker run -p 8000:8000 ocr-service
```

The API will be accessible at:

```
http://localhost:8000
```

---

## Notes on PDF Validation

Uploaded files are validated using a PDF parser before OCR processing. This ensures that only real, parseable PDF documents are accepted by the service, improving robustness and security when deployed as a public API.

---

## License

This project is provided as-is. Add license information here if applicable.
