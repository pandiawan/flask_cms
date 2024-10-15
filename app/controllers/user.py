from flask import jsonify, request
from app.services.user import UserService
from app.schemas.user import UserSchema


class UserController:
    def __init__(self):
        self.user_service = UserService()
        self.user_schema = UserSchema()

    def create(self):
        data = request.get_json()
        errors = self.user_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        user_id = self.user_service.create(
            name=data['name'],
            email=data['email'],
            username=data['username'],
            password=data['password']
        )

        user = self.user_service.get_by_id(user_id)
        user_data = self.user_schema.dump(user)
        return jsonify({'_id': str(user_id), **user_data}), 201

    def get_by_id(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user_data = self.user_schema.dump(user)
        return jsonify(user_data), 200

    def get_all(self):
        users = self.user_service.get_all()
        user_list = list(users)
        users_data = self.user_schema.dump(user_list, many=True)
        return jsonify(users_data), 200

    def update(self, user_id):
        data = request.get_json()
        errors = self.user_schema.validate(data, partial=True)
        if errors:
            return jsonify(errors), 400

        updated_user = self.user_service.update(user_id, data)
        if not updated_user:
            return jsonify({'error': 'User not found'}), 404

        user = self.user_service.get_by_id(user_id)
        user_data = self.user_schema.dump(user)
        return jsonify({'_id': str(user_id), **user_data}), 200

    def delete(self, user_id):
        success = self.user_service.delete(user_id)
        if not success:
            return jsonify({"message": "User not found"}), 404

        return jsonify({'message': 'Successfully deleted the category'}), 204
