from datetime import datetime
from utils.db import db

class Tutorial:
    collection = db.tutorials

    @staticmethod
    def create_tutorial(title, description, content, category, author_id):
        tutorial = {
            "title": title,
            "description": description,
            "content": content,  # Can include notes, images, video links
            "category": category,
            "author_id": author_id,
            "created_at": datetime.utcnow(),
        }
        return Tutorial.collection.insert_one(tutorial)

    @staticmethod
    def get_tutorials():
        return list(Tutorial.collection.find({}))

class User:
    collection = db.users

    @staticmethod
    def create_user(username, email, password):
        user = {
            "username": username,
            "email": email,
            "password": password,  # Hash this in production!
            "created_at": datetime.utcnow(),
        }
        return User.collection.insert_one(user)