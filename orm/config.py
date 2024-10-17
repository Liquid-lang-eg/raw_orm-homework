from connection import DB_CONNECTION

class Settings:

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def DATABASE_URL(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


settings = Settings(**DB_CONNECTION)
