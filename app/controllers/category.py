from flask import jsonify, request
from app.services.category import CategoryService
from app.schemas.category import CategorySchema


class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()
        self.category_schema = CategorySchema()

    def create(self):
        data = request.get_json()
        errors = self.category_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        category_id = self.category_service.create(data)

        category = self.category_service.get_by_id(category_id)
        category_data = self.category_schema.dump(category)
        return jsonify({'_id': str(category_id), **category_data}), 201

    def get_all(self):
        categories = self.category_service.get_all()
        categories_list = list(categories)
        categories_data = self.category_schema.dump(categories_list, many=True)
        return jsonify(categories_data), 200

    def get_by_id(self, category_id):
        category = self.category_service.get_by_id(category_id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        category_data = self.category_schema.dump(category)
        return jsonify(category_data), 200

    def update(self, category_id):
        data = request.get_json()
        errors = self.category_schema.validate(data, partial=True)
        if errors:
            return jsonify(errors), 400

        updated_category = self.category_service.update(category_id, data)
        if not updated_category:
            return jsonify({'error': 'Category not found'}), 404

        category = self.category_service.get_by_id(category_id)
        category_data = self.category_schema.dump(category)
        return jsonify({'_id': str(category_id), **category_data}), 200

    def delete(self, category_id):
        success = self.category_service.delete(category_id)
        if not success:
            return jsonify({'error': 'Category not found'}), 404

        return jsonify({'message': 'Successfully deleted the category'}), 204
