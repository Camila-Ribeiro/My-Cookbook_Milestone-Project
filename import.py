import os
import requests
from pprint import pprint
import pymongo

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myCookbookDB"
COLLECTION_NAME = "myFistBookMDB"

def mongo_connect(url):
    """Function to make a connection to our DB"""
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

conn = mongo_connect(MONGODB_URI)  # Assign our connection to a var
coll = conn[DBS_NAME][COLLECTION_NAME]  # Put it all together




# return recipes
# pprint(recipes)