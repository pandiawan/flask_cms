from flask import Blueprint
from flasgger.utils import swag_from
from app.controllers.category import CategoryController
from flask_jwt_extended import jwt_required

category_bp = Blueprint('category', __name__)


@category_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from('../docs/category/add.yml')
def create():
    return CategoryController().create()


@category_bp.route('/', methods=['GET'])
@jwt_required()
@swag_from('../docs/category/get_all.yml')
def get_all():
    return CategoryController().get_all()


@category_bp.route('/<string:category_id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/category/get_by_id.yml')
def get_by_id(category_id):
    return CategoryController().get_by_id(category_id)


@category_bp.route('/<string:category_id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/category/update.yml')
def update(category_id):
    return CategoryController().update(category_id)


@category_bp.route('/<string:category_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/category/delete.yml')
def delete(category_id):
    return CategoryController().delete(category_id)
