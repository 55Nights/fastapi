from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_password: str
    database_port: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = '.env'


settings = Settings()
