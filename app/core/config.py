import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator


class Settings():
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl = "localhost"
    SERVER_PORT: int = 8000
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["*"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """
        Validator function for assembling CORS origins.

        Args:
            cls: The class object.
            v: The input value to be validated.

        Returns:
        The validated value.

        Raises:
            ValueError: If the input value is not a string or a list.
        """
        # If the input value is a string and does not start with '[', split it by comma and strip each element
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        # If the input value is a list or a string, return it as is
        elif isinstance(v, (list, str)):
            return v
        # Raise ValueError if the input value is neither a string nor a list
        raise ValueError(v)


settings = Settings()
