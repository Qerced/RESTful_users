from fastapi_users_db_beanie import PydanticObjectId
from pydantic import BaseModel, Field


class BaseMessage(BaseModel):
    _id: PydanticObjectId
    sender_id: PydanticObjectId
    recipient_id: PydanticObjectId
    dialog_id: PydanticObjectId
    content: str


class CreateMessage(BaseModel):
    recipient_id: PydanticObjectId
    content: str


class ReadMessage(BaseModel):
    dialog_id: PydanticObjectId = Field(..., alias="_id")
    messages: list[BaseMessage]
