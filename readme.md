# FastAPI PDF Analysis and Chat Application

This project is a FastAPI application that allows you to upload PDF files, analyze their content, and engage in conversations about the PDF content using Google's Gemini AI model.

## 🚀 Features

- Upload PDF files and extract text
- AI-supported chat based on PDF content
- Detailed logging system
- RESTful API endpoints
- API documentation with Swagger UI
- CORS support

## 📋 Requirements

- Python 3.8+
- FastAPI
- PyMuPDF
- Google Generative AI
- Other dependencies are listed in the `requirements.txt` file

## 🛠️ Installation

### 1. Clone the Project:

```bash
git clone https://github.com/MustafaKorukmez/fastapi_llm.git
cd fastapi_llm
```

### 2. Create and Activate a Virtual Environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables:

Create a `.env` file:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🚀 Running the Application

```bash
uvicorn app.main:app --reload
```

The application will run at `http://localhost:8000` by default.

## 📚 API Documentation

To test the API and view the documentation:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔄 API Endpoints

### PDF Upload

```http
POST /api/upload-pdf/
```

Used to upload a PDF file.

#### Example cURL:

```bash
curl -X POST "http://localhost:8000/api/upload-pdf/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/document.pdf"
```

### Chat

```http
POST /api/chat/
```

Used to ask questions about the uploaded PDF content.

#### Example Request:

```json
{
    "message": "What are the main topics in the PDF content?"
}
```

## 📁 Project Structure

```
fastapi_llm/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── pdf.py
│   │   │   └── chat.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── chat.py
│   └── services/
│       ├── __init__.py
│       ├── pdf_service.py
│       └── gemini_service.py
├── requirements.txt
└── README.md
```

## 🔍 Key Components

- **api/**: Contains the API endpoints
- **core/**: Contains core configuration and logging settings
- **models/**: Contains Pydantic models
- **services/**: Contains business logic services

## 📝 Logging

The application maintains detailed log records:

- System logs: `app.log`
- Error logs
- Transaction logs

To view the log file:

```bash
tail -f app.log
```

## 🔒 Security Notes

1. Safely store your API key
2. Add the `.env` file to `.gitignore` in production environments
3. Implement rate limiting
4. Add file size restrictions

## 🚧 Known Limitations

- Currently, only PDF files are supported
- Maximum file size limit: 10MB
- Only one PDF file can be processed per session

## 🔄 Development Recommendations

1. **Database Integration**
   - To store PDF content permanently
   - To manage user sessions

2. **Security Enhancements**
   - Add JWT authentication
   - Implement rate limiting
   - Improve file type validation

3. **Performance Enhancements**
   - Asynchronous queue system for PDF processing
   - Caching mechanism
   - Support for streaming large files

## 🐛 Troubleshooting

Common errors and their solutions:

1. **404 Not Found**
   - Ensure the API path is correct
   - Make sure you are using the `/api/` prefix

2. **400 Bad Request**
   - Check that the PDF file is in the correct format
   - Ensure the request body is properly structured

3. **500 Internal Server Error**
   - Check the log files
   - Ensure the API key is correct


## 📞 Contact

- Project Owner: [Linkedin](https://www.linkedin.com/in/mustafakorukmez/), [GitHub](https://github.com/MustafaKorukmez)
- Project Link: [GitHub](https://github.com/MustafaKorukmez/ask_my_pdf)

## 🙏 Acknowledgements

- To the FastAPI team
- To the Google Gemini AI team
- To all contributors

---
