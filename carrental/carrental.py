import os
import json
import pymongo
import pprint
from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://swatinarkhede:sjsu123@zipcardbcluster-hjwsb.mongodb.net/test?retryWrites=true&w=majority")

db = client['test']
collection = db['posts1']
print("Done")


post = {"username": "Albert",
        "email_id": "albert2@gmail.com",
        "Password": "test123",
        "Gender": "Male"}

post_id = collection.insert_one(post).inserted_id
print(post_id)

print("Added one record")
pprint.pprint(collection.find_one({"user": "Swati"}))
