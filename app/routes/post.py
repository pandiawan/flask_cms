from flask import Blueprint
from flasgger.utils import swag_from
from app.controllers.post import PostController
from flask_jwt_extended import jwt_required

post_bp = Blueprint('post', __name__)


@post_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from('../docs/post/add.yml')
def create():
    return PostController().create()


@post_bp.route('/', methods=['GET'])
@jwt_required()
@swag_from('../docs/post/get_all.yml')
def get_all():
    return PostController().get_all()


@post_bp.route('/<string:post_id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/post/get_by_id.yml')
def get_by_id(post_id):
    return PostController().get_by_id(post_id)


@post_bp.route('/<string:post_id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/post/update.yml')
def update(post_id):
    return PostController().update(post_id)


@post_bp.route('/<string:post_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/post/delete.yml')
def delete(post_id):
    return PostController().delete(post_id)
