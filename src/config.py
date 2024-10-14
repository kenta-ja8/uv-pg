import os
from pydantic import BaseModel
from dotenv import load_dotenv


def load_config():
    _ = load_dotenv(".env")
    return Config(
        SAMPLE_BASE_URL=os.getenv("SAMPLE_BASE_URL", ""),
        SAMPLE_API_KEY=os.getenv("SAMPLE_API_KEY", ""),
    )


class Config(BaseModel):
    SAMPLE_BASE_URL: str
    SAMPLE_API_KEY: str
