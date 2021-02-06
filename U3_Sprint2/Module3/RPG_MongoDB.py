# I would say using SQL seems a little more straight forward but 
# MongoDB seems more equipped to handle large amounts of data and
# it is easier to navigate using MongoDB.


import pymongo
import os
from dotenv import load_dotenv
from pprintpp import pprint
import pandas as pd
import json

# db_user = os.getenv("mod3_user")
# db_pwd = os.getenv("mod3_pwd")
# db_cluster_name = os.getenv("mod3_cln")
# db_name = "RPG_MongoDB"

db_pwd = "Northeast1212"
db_name = "RPG_MongoDB"

# Using the getenv method of hiding sensitive information I ran into
# multiple authentification issues requiring parse encoding and quoting.
client = pymongo.MongoClient("mongodb+srv://Cknowles11:{}@cluster0.uyjbe.mongodb.net/{}?retryWrites=true&w=majority".format(db_pwd, db_name))
print("CLIENT:", type(client), client)

db = client.RPG_MongoDB
print("-----------------")
print("DB:", type(db), db)

print("-----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection = db.character
print(" ")
print("Collections:", type(collection), collection)

with open("charactercreator_character.json") as ccc:
    c_data = json.load(ccc)

collection.insert_many(c_data)

collection = db.character_inventory
print(" ")
print("Collections:", type(collection), collection)

with open("charactercreator_character_inventory.json") as cci:
    ci_data = json.load(cci)

collection.insert_many(ci_data)

collection = db.armory_item
print(" ")
print("Collections:", type(collection), collection)

with open("armory_item.json") as ai:
    ai_data = json.load(ai)

collection.insert_many(ai_data)

collection = db.armory_weapon
print(" ")
print("Collections:", type(collection), collection)

with open("armory_weapon.json") as aw:
    aw_data = json.load(aw)

collection.insert_many(aw_data)