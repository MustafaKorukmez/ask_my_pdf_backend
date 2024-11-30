import fitz
from app.core.logging import get_logger

logger = get_logger(__name__)

class PDFService:
    @staticmethod
    async def extract_text(file_contents: bytes) -> str:
        logger.info("Starting PDF text extraction")
        try:
            with fitz.open(stream=file_contents, filetype="pdf") as pdf_document:
                text = ""
                for page_num, page in enumerate(pdf_document, 1):
                    logger.debug(f"Processing page {page_num}")
                    text += page.get_text()
                
                logger.info(f"PDF text extraction completed successfully. Processed {page_num} pages.")
                return text
        except Exception as e:
            logger.error(f"PDF processing error: {str(e)}")
            raise Exception(f"Error processing PDF: {str(e)}")