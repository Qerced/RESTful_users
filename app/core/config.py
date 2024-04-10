from pydantic_settings import BaseSettings

APP_TITLE_DEFAULT = 'RESTful_users'
DATABASE_URL = 'mongodb://{username}:{password}@{host}:{port}'
SECRET_DEFAULT = 'SECRET'
ENV_FILE = '.env'


class Settings(BaseSettings):
    debug: bool = True
    app_title: str = APP_TITLE_DEFAULT
    secret: str = SECRET_DEFAULT
    db_host: str
    db_port: str
    mongo_initdb_root_username: str
    mongo_initdb_root_password: str

    @property
    def database_url(self):
        return DATABASE_URL.format(
            username=self.mongo_initdb_root_username,
            password=self.mongo_initdb_root_password,
            host=self.db_host if not self.debug else 'localhost',
            port=self.db_port,
        )

    class Config:
        env_file = ENV_FILE


settings = Settings()
