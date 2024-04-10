from fastapi import FastAPI

from app.api.routers import main_router
from app.core.db import lifespan
from app.core.config import settings

app = FastAPI(lifespan=lifespan, title=settings.app_title)

app.include_router(main_router)
