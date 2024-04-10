from beanie import Document
from fastapi_users_db_beanie import PydanticObjectId


class DialogModel(Document):
    sender_id: PydanticObjectId
    recipient_id: PydanticObjectId

    @classmethod
    async def get_or_create(
        self, sender_id: PydanticObjectId, recipient_id: PydanticObjectId
    ) -> 'DialogModel':
        if dialog := await self.find_one({'$or': [
            {'sender_id': sender_id, 'recipient_id': recipient_id},
            {'sender_id': recipient_id, 'recipient_id': sender_id}
        ]}):
            return dialog
        else:
            return await self(
                sender_id=sender_id, recipient_id=recipient_id
            ).insert()
