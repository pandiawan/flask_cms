from flask import request, jsonify, current_app
from app.schemas.post import PostSchema
from app.services.post import PostService
from app.services.tag import TagService
from app.helpers import image
from flask_jwt_extended import get_jwt_identity


class PostController:
    def __init__(self):
        self.post_service = PostService()
        self.post_schema = PostSchema()
        self.tag_service = TagService()

    def create(self):
        data = request.form.to_dict()
        author_id = get_jwt_identity()
        data['author'] = str(author_id)

        params_tags = data['tags'].split(',')
        tags = []
        for tag_name in params_tags:
            tag_name = tag_name.strip()
            existing_tag = self.tag_service.get_by_name(tag_name)

            if existing_tag:
                tags.append(existing_tag['name'])
            else:
                tag_id = self.tag_service.create({'name': tag_name})
                tag = self.tag_service.get_by_id(tag_id)
                tags.append(tag['name'])

        data['tags'] = tags
        if 'image' not in request.files:
            return jsonify({"message": "No image part"}), 400

        file = request.files['image']
        upload_image, err = image.upload(file, current_app.config['IMAGE_FOLDER'])
        if not err:
            data['image'] = upload_image
        else:
            return jsonify({"message": "Invalid file format"}), 400

        errors = self.post_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        post_id = self.post_service.create(data)
        post = self.post_service.get_by_id(post_id)
        post_data = self.post_schema.dump(post)
        return jsonify({'_id': str(post_id), **post_data}), 201

    def get_all(self):
        posts = self.post_service.get_all()
        post_list = list(posts)
        posts_data = self.post_schema.dump(post_list, many=True)
        return jsonify(posts_data), 200

    def get_by_id(self, post_id):
        post = self.post_service.get_by_id(post_id)
        if not post:
            return jsonify({'error': 'Post not found'}), 404

        post_data = self.post_schema.dump(post)
        return jsonify(post_data), 200

    def update(self, post_id):
        data = request.form.to_dict()
        params_tags = data['tags'].split(',')
        tags = []
        for tag_name in params_tags:
            tag_name = tag_name.strip()
            existing_tag = self.tag_service.get_by_name(tag_name)

            if existing_tag:
                tags.append(existing_tag['name'])
            else:
                tag_id = self.tag_service.create({'name': tag_name})
                tag = self.tag_service.get_by_id(tag_id)
                tags.append(tag['name'])

        data['tags'] = tags

        if 'image' in request.files:
            file = request.files['image']
            upload_image, err = image.upload(file, current_app.config['IMAGE_FOLDER'])
            if not err:
                data['image'] = upload_image
            else:
                return jsonify({"message": "Invalid file format"}), 400

        errors = self.post_schema.validate(data, partial=True)
        if errors:
            return jsonify(errors), 400

        updated_post = self.post_service.update(post_id, data)
        if not updated_post:
            return jsonify({'error': 'Post not found'}), 404

        post = self.post_service.get_by_id(post_id)
        post_data = self.post_schema.dump(post)
        return jsonify({'_id': str(post_id), **post_data}), 200

    def delete(self, post_id):
        success = self.post_service.delete(post_id)
        if not success:
            return jsonify({'error': 'Post not found'}), 404

        return jsonify({'message': 'Successfully deleted the post'}), 204
