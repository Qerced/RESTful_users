from fastapi import APIRouter, Depends

from app.api.endpoints.validators import check_exists_user
from app.core.user import current_user
from app.models import DialogModel, MessageModel, UserModel
from app.schemas.message import BaseMessage, CreateMessage, ReadMessage


router = APIRouter()


@router.post('/create', response_model=BaseMessage)
async def create_message(
    message: CreateMessage, user: UserModel = Depends(current_user)
):
    await check_exists_user(message.recipient_id)
    dialog = await DialogModel.get_or_create(user.id, message.recipient_id)
    return await MessageModel(
        sender_id=user.id, recipient_id=message.recipient_id,
        dialog_id=dialog.id, content=message.content
    ).insert()


@router.get('/get', response_model=list[ReadMessage])
async def get_messages(user: UserModel = Depends(current_user)):
    return await MessageModel.find(
        {'$or': [{'recipient_id': user.id}, {'sender_id': user.id}]}
    ).aggregate(
        [{'$group': {'_id': '$dialog_id', 'messages': {'$push': '$$ROOT'}}}]
    ).to_list()
