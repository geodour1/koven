from helpers.logger import Logger
from models.user import User

from pymongo import MongoClient
from typing import List

import os

class DBConnector:
    COLLECTION_USER = 'collection_user'
    COLLECTION_GRAPH = 'collection_graph'
    DATABASE = 'application'
    
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv("DB_HOST", ""))
            self.db = self.client.get_database(self.DATABASE)
            
            Logger.log_success("Connected to mongo.")
        except Exception as e:
            Logger.log_error("Failed to connect to mongo.")
            Logger.log_error(e)
    
    def user_insert_one(self, user:User)->User:
        user_id = self.db.get_collection(self.COLLECTION_USER).insert_one(user.to_json()).inserted_id
        updated_user_doc = self.db.get_collection(self.COLLECTION_USER).find_one({'_id': user_id})
        updated_user = User.from_doc(updated_user_doc)
        return updated_user
    
    def user_all(self)->List[User]:
        users = []
        for user_doc in self.db.get_collection(self.COLLECTION_USER).find({}):
            user = User.from_doc(user_doc)
            users.append(user.to_json(include_id=True))
        
        return users
