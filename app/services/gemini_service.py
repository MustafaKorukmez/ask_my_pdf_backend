import google.generativeai as genai
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

class GeminiService:
    def __init__(self):
        self.setup_api()
    
    def setup_api(self):
        logger.info("Configuring Gemini API")
        try:
            genai.configure(api_key=settings.GOOGLE_API_KEY)
            logger.info("Gemini API configured successfully")
        except Exception as e:
            logger.error(f"Gemini API configuration error: {str(e)}")
            raise

    async def generate_response(self, prompt: str) -> str:
        logger.info("Requesting response from Gemini API")
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            logger.info("Successfully received response from Gemini API")
            return response.text
        except Exception as e:
            logger.error(f"Gemini API response error: {str(e)}")
            raise 