from flask import Blueprint
from flasgger.utils import swag_from
from app.controllers.user import UserController
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from('../docs/user/add.yml')
def create():
    return UserController().create()


@user_bp.route('/', methods=['GET'])
@jwt_required()
@swag_from('../docs/user/get_all.yml')
def get_all():
    return UserController().get_all()


@user_bp.route('/<string:user_id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/user/get_by_id.yml')
def get_by_id(user_id):
    return UserController().get_by_id(user_id)


@user_bp.route('/<string:user_id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/user/update.yml')
def update(user_id):
    return UserController().update(user_id)


@user_bp.route('/<string:user_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/user/delete.yml')
def delete(user_id):
    return UserController().delete(user_id)
