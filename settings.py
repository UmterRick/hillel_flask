from pydantic_settings import BaseSettings

<<<<<<< HEAD

class Settings(BaseSettings):
    DB_URL:str

    class Config:
        env_file = ".env"


settings = Settings()
=======
class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file=".env"


settings = Settings()


# from pydantic_settings import BaseSettings
# from typing import Optional
#
# class Settings(BaseSettings):
#     DB_URL: str = "sqlite:///database.db"  # default value
#     SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
#     SQLALCHEMY_DATABASE_URI: Optional[str] = None
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.SQLALCHEMY_DATABASE_URI = self.DB_URL
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         case_sensitive = True
#
#
# settings = Settings()
>>>>>>> 5d80988 (flask project)
