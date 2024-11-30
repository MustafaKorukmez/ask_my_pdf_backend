from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    API_V1_STR: str = Field(default="/api")
    PROJECT_NAME: str = Field(default="FastAPI LLM Application")
    GOOGLE_API_KEY: str = Field(default='AIzaSyCc3mnjuImVdbPaaDuPoSByjK8xmbkhga8')

    class Config:
        env_file = ".env"

settings = Settings() 