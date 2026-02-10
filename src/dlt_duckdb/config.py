from pydantic import Field
from pydantic_settings import BaseSettings
from typing_extensions import Annotated
from pathlib import Path

class Settings(BaseSettings):

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }
    POKEMON_API: Annotated[str, Field()]
    DATA_DIR: Annotated[Path, Field(default=Path("data"))]