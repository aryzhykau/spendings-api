from pymongo import MongoClient


class MongoDB:
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(f"mongodb://myuser:mypassword@{self.host}:{self.port}/")
        self.db = self.client[self.database]


    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None


    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

