from bson import ObjectId
from flask import current_app as app


class TagService:
    def __init__(self):
        self.collection = app.mongo.db.tags

    def create(self, data):
        tag_data = {
            'name': data['name'],
        }
        result = self.collection.insert_one(tag_data)
        return str(result.inserted_id)

    def get_by_id(self, tag_id):
        tag = self.collection.find_one({'_id': ObjectId(tag_id)})
        if tag:
            tag['_id'] = str(tag['_id'])
        return tag

    def get_by_name(self, name):
        tag = self.collection.find_one({"name": name})
        if tag:
            tag['_id'] = str(tag['_id'])
        return tag

    def get_all(self):
        tags = self.collection.find()
        return tags

    def update(self, tag_id, updated_data):
        tag = self.collection.find_one_and_update({'_id': ObjectId(tag_id)}, {'$set': updated_data})
        if tag:
            tag['_id'] = str(tag['_id'])
        return tag

    def delete(self, tag_id):
        result = self.collection.delete_one({'_id': ObjectId(tag_id)})
        return result.deleted_count > 0
