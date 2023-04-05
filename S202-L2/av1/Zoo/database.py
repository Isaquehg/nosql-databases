import glob
import importlib

# adapting imports dinamically
modules = glob.glob("Zoo/*.py")
for module in modules:
    module_name = module.split("/")[-1].split(".")[0]
    importlib.import_module(f"Zoo.{module_name}")

import pymongo

# database connection class
class DatabaseClass:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Database reseted successfully!")
        except Exception as e:
            print(e)