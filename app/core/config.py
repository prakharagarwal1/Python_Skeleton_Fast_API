from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Assistant"
    app_env: str = "development"
    app_port: int = 8000

    openai_api_key: str = ""
    groq_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()