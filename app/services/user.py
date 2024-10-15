from werkzeug.security import check_password_hash, generate_password_hash
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from flask import current_app as app


class UserService:
    def __init__(self):
        self.collection = app.mongo.db.users

    def create(self, name, email, username, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user_data = {
            "name": name,
            "email": email,
            "username": username,
            "password": hashed_password
        }
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    def get_by_id(self, user_id):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
        return user

    def get_by_username(self, username):
        user = self.collection.find_one({"username": username})
        if user:
            user['_id'] = str(user['_id'])
        return user

    def get_all(self):
        users = self.collection.find()
        return users

    def update(self, user_id, updated_data):
        if "password" in updated_data:
            updated_data["password"] = generate_password_hash(updated_data["password"], method='pbkdf2:sha256')

        user = self.collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data},
            return_document=ReturnDocument.AFTER
        )
        if user:
            user['_id'] = str(user['_id'])
        return user

    def delete(self, user_id):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    def authenticate(self, username, password):
        user = self.get_by_username(username)
        if user and check_password_hash(user['password'], password):
            user['_id'] = str(user['_id'])
            return user
        return None
