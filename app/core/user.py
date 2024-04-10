import re
import string

from fastapi import Depends
from fastapi_users import (
    BaseUserManager, FastAPIUsers, InvalidPasswordException
)
from fastapi_users.authentication import (
    AuthenticationBackend, BearerTransport, JWTStrategy
)
from fastapi_users_db_beanie import BeanieUserDatabase, ObjectIDIDMixin

from app.core.config import settings
from app.models import UserModel
from app.schemas.user import UserCreate

TOKEN_URL = 'auth/jwt/login'
REASON_PASSWORD = 'Password should be at least 3 characters'


async def get_user_db():
    yield BeanieUserDatabase(UserModel)

bearer_transport = BearerTransport(tokenUrl=TOKEN_URL)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(ObjectIDIDMixin, BaseUserManager[UserModel, int]):
    async def validate_password(
            self, password: str, user: UserCreate | UserModel
    ) -> None:
        if re.fullmatch(
            f'[{re.escape(string.ascii_letters + string.digits)}]{{3,20}}',
            password
        ) is None:
            raise InvalidPasswordException(
                reason=REASON_PASSWORD
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[UserModel, ObjectIDIDMixin](
    get_user_manager, [auth_backend],
)
current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
