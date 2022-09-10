from pymongo import MongoClient
import os

password = os.environ.get("MongoDBPassword")
client = MongoClient(f"mongodb+srv://Ganyu-bot-cloud-db:{password}@ganyu-bot.7pvjkku.mongodb.net/?retryWrites=true&w=majority")

class MongoDB:
    def __init__(self, db:str, collection:str) -> None:
        self.col = client[str(db)][str(collection)]

        self.OPERATE = {
            "or":"$or",
            "in":"$in",
            "all":"$all",
            "not_in":"$nin",
            "<":"$lt",
            "<=":"$lte",
            ">":"$gt",
            ">=":"$gte",
        }

    def set(self, data:dict):
        self.col.insert_one(data)

    def set_many(self, data:list):
        self.col.insert_many(data)

    def update(self, query, new:dict):
        self.col.update_one(query,{"$set":new})

    def update_all(self, query, new):
        self.col.update_many(query,{"$set":new})

    def read_first(self, query:dict={}, id:int=0):
        return self.col.find_one( query,{"_id":id})

    def read_all(self, query:dict={}, is_read:dict={}, id:bool=False):
        """
            Parameters
            ==========
            query: :class:`dict`
            -------------------
                conditions to filter
                ### Support Operation

                    or : `{"$or":query}`

                    all : `{"$all":query}`

                    in : `{query:{"$in":[]}}`
                    
                    not in : `{query:{"$nin":[]}}`
                    
                    < : `{query:{"$lt":`int`}}`

                    <= : `{query:{"$lte:`int`}}`

                    ">": `{"query":{"$gt":`int`}}`

                    ">=": `{"query"{"$gte":`int`}}`
        """
        
        is_read["_id"] = 0 if id == False else 1

        datas = [data for data in self.col.find(query,is_read)]
        return datas

    def delete(self, data):
        self.col.delete_one(data)

    def delete_all(self, query:dict={}):
        self.col.delete_many(query)

    def drop(self):
        self.col.drop()

    @property
    def data(self):
        return self.read_all()

#Syntax help: https://iter01.com/443447.html