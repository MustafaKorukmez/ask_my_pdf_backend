from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.gemini_service import GeminiService
from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.post("/chat/", response_model=ChatResponse)
async def chat_with_pdf(chat_request: ChatRequest):
    from app.api.endpoints.pdf import pdf_content
    
    if not pdf_content:
        logger.warning("No PDF content found")
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file first"
        )
    
    try:
        logger.info(f"Chat request received: {chat_request.message[:50]}...")
        gemini_service = GeminiService()
        
        prompt = f"""
        Please answer the question based on the following PDF content:
        
        PDF Content:
        {pdf_content}
        
        Question: {chat_request.message}
        """
        
        response = await gemini_service.generate_response(prompt)
        logger.info("Chat response generated successfully")
        
        return ChatResponse(response=response)
    except Exception as e:
        logger.error(f"Chat processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 