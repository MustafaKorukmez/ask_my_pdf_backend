from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.pdf_service import PDFService
from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)

# PDF content storage (in a real application, a database should be used)
pdf_content = ""

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    global pdf_content
    
    # Log incoming file details
    logger.info(f"Incoming file: {file.filename}, Content-Type: {file.content_type}")
    
    if not file.filename.endswith('.pdf'):
        logger.error(f"Invalid file format: {file.filename}")
        raise HTTPException(
            status_code=400, 
            detail=f"Only PDF files are accepted. Received file: {file.filename}"
        )
    
    try:
        contents = await file.read()
        logger.info(f"File size: {len(contents)} bytes")
        
        pdf_content = await PDFService.extract_text(contents)
        
        logger.info(f"PDF processed successfully: {file.filename}")
        return {
            "message": "PDF uploaded successfully",
            "filename": file.filename,
            "content_preview": pdf_content[:200] + "..."  # Show first 200 characters
        }
    except Exception as e:
        logger.error(f"PDF processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}") 