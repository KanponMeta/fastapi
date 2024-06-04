from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import SessionLocal
from app.db import init_db


app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix='/api')

if __name__ == "__main__":
    init_db.init_db()
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)