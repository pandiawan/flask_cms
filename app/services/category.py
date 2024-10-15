from bson import ObjectId
from flask import current_app as app


class CategoryService:
    def __init__(self):
        self.collection = app.mongo.db.categories

    def create(self, data):
        category_data = {
            'name': data['name'],
        }
        result = self.collection.insert_one(category_data)
        return str(result.inserted_id)

    def get_by_id(self, category_id):
        category = self.collection.find_one({'_id': ObjectId(category_id)})
        if category:
            category['_id'] = str(category['_id'])
        return category

    def get_all(self):
        categories = self.collection.find()
        return categories

    def update(self, category_id, updated_data):
        category = self.collection.find_one_and_update({'_id': ObjectId(category_id)}, {'$set': updated_data})
        if category:
            category['_id'] = str(category['_id'])
        return category

    def delete(self, category_id):
        result = self.collection.delete_one({'_id': ObjectId(category_id)})
        return result.deleted_count > 0
