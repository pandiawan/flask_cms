from flask import jsonify, request
from flask_jwt_extended import create_access_token
from app.services.user import UserService


class AuthController:
    def __init__(self):
        self.user_model = UserService()

    def login(self):
        data = request.get_json()
        user = self.user_model.authenticate(data['username'], data['password'])
        if user:
            access_token = create_access_token(identity=user['_id'])
            return jsonify(access_token=access_token), 200
        return jsonify({"message": "Bad username or password"}), 401
