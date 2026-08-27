from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    DEFAULT_LLM_PROVIDER: str
    DEFAULT_OPENAI_MODEL: str
    DEFAULT_ANTHROPIC_MODEL: str
    DB_HOST: str
    DB_USER_NAME: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()

