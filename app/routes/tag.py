from flask import Blueprint
from flasgger.utils import swag_from
from app.controllers.tag import TagController
from flask_jwt_extended import jwt_required

tag_bp = Blueprint('tag', __name__)


@tag_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from('../docs/tag/add.yml')
def create():
    return TagController().create()


@tag_bp.route('/', methods=['GET'])
@jwt_required()
@swag_from('../docs/tag/get_all.yml')
def get_all():
    return TagController().get_all()


@tag_bp.route('/<string:tag_id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/tag/get_by_id.yml')
def get_by_id(tag_id):
    return TagController().get_by_id(tag_id)


@tag_bp.route('/<string:tag_id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/tag/update.yml')
def update(tag_id):
    return TagController().update(tag_id)


@tag_bp.route('/<string:tag_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/tag/delete.yml')
def delete(tag_id):
    return TagController().delete(tag_id)
