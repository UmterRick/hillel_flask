import os

class Settings:
    def __init__(self):
        # Default to SQLite if DB_URL is not provided
        self.DB_URL = os.getenv('DB_URL', 'sqlite:///students.db')

settings = Settings()