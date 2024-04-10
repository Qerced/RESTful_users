from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.models import DialogModel, MessageModel, UserModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie(
        database=AsyncIOMotorClient(settings.database_url).app,
        document_models=[
            DialogModel, MessageModel, UserModel
        ],
    )
    yield
