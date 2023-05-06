import os
import pymongo
import certifi
from dotenv import load_dotenv
ca = certifi.where()
load_dotenv()

class MongodbClient:
    client = None

    def __init__(self,) -> None:
        database_name = 'flipkart'
        if MongodbClient.client is None:
            mongo_db_url = os.getenv("MONGO_DB_URL_ENV_KEY")
            if mongo_db_url is None:
                raise Exception('Environment key: {"MONGO_DB_URL_ENV_KEY"} is not set.')
            MongodbClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name