from flask import current_app as app
from bson import ObjectId


class PostService:
    def __init__(self):
        self.collection = app.mongo.db.posts

    def create(self, data):
        post_data = {
            'title': data['title'],
            'content': data['content'],
            'image': data['image'],
            'author': data['author'],
            'category_id': data['category_id'],
            'tags': data['tags']
        }
        result = self.collection.insert_one(post_data)
        return str(result.inserted_id)

    def get_by_id(self, post_id):
        post = self.collection.find_one({'_id': ObjectId(post_id)})
        if post:
            post['_id'] = str(post['_id'])
        return post

    def get_all(self):
        posts = self.collection.find()
        return posts

    def update(self, post_id, updated_data):
        post = self.collection.find_one_and_update({'_id': ObjectId(post_id)}, {'$set': updated_data})
        if post:
            post['_id'] = str(post['_id'])
        return post

    def delete(self, post_id):
        result = self.collection.delete_one({'_id': ObjectId(post_id)})
        return result.deleted_count > 0
