from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import pdf, chat
from app.core.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="FastAPI LLM Application",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers
app.include_router(
    pdf.router, 
    prefix=settings.API_V1_STR,
    tags=["pdf"]
)
app.include_router(
    chat.router, 
    prefix=settings.API_V1_STR,
    tags=["chat"]
)

@app.on_event("startup")
async def startup_event():
    logger.info("Application is starting up")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application is shutting down")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI LLM Application!"} 