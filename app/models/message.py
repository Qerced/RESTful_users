from beanie import Document
from fastapi_users_db_beanie import PydanticObjectId


class MessageModel(Document):
    sender_id: PydanticObjectId
    recipient_id: PydanticObjectId
    dialog_id: PydanticObjectId
    content: str
