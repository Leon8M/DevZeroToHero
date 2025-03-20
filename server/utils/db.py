from pymongo import MongoClient
from flask import current_app

def init_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/devzerotohero"
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.get_database()