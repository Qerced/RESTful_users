from http import HTTPStatus

from fastapi import HTTPException
from fastapi_users_db_beanie import PydanticObjectId

from app.models import UserModel

NOT_FOUND = 'User with this id does not exist'


async def check_exists_user(id: PydanticObjectId) -> None:
    if not await UserModel.find_one({'_id': id}):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=NOT_FOUND)
