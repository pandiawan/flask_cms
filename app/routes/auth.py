from flask import Blueprint
from flasgger.utils import swag_from
from app.controllers.auth import AuthController

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['POST'])
@swag_from('../docs/auth/login.yml')
def login_route():
    return AuthController().login()
