from flask import request, jsonify
from app.schemas.tag import TagSchema
from app.services.tag import TagService


class TagController:
    def __init__(self):
        self.tag_service = TagService()
        self.tag_schema = TagSchema()

    def create(self):
        data = request.get_json()
        errors = self.tag_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        tag_id = self.tag_service.create(data)

        tag = self.tag_service.get_by_id(tag_id)
        tag_data = self.tag_schema.dump(tag)
        return jsonify({'_id': str(tag_id), **tag_data}), 201

    def get_all(self):
        tags = self.tag_service.get_all()
        tags_list = list(tags)
        tags_data = self.tag_schema.dump(tags_list, many=True)
        return jsonify(tags_data), 200

    def get_by_id(self, tag_id):
        tag = self.tag_service.get_by_id(tag_id)
        if not tag:
            return jsonify({'error': 'Tag not found'}), 404

        tag_data = self.tag_schema.dump(tag)
        return jsonify(tag_data), 200

    def update(self, tag_id):
        data = request.get_json()
        errors = self.tag_schema.validate(data, partial=True)
        if errors:
            return jsonify(errors), 400

        updated_tag = self.tag_service.update(tag_id, data)
        if not updated_tag:
            return jsonify({'error': 'Tag not found'}), 404

        tag = self.tag_service.get_by_id(tag_id)
        tag_data = self.tag_schema.dump(tag)
        return jsonify({'_id': str(tag_id), **tag_data}), 200

    def delete(self, tag_id):
        success = self.tag_service.delete(tag_id)
        if not success:
            return jsonify({'error': 'Tag not found'}), 404

        return jsonify({'message': 'Successfully deleted the tag'}), 204
