import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from config import config_by_name
from flasgger import Swagger
from mongomock import MongoClient as MongoMockClient
from flask_jwt_extended import JWTManager

marshmallow = Marshmallow()
jwt = JWTManager()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask CMS API",
        "description": "API documentation for Flask CMS",
        "version": "1.0.0",
        "contact": {
            "name": "Nana Pandiawan",
            "url": "https://pengerat.net",
            "email": "nana@pengerat.net"
        }
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }

}

swagger = Swagger(template=swagger_template)


def create_app(config_name=None):
    app = Flask(__name__)

    config_name = config_name or os.getenv('FLASK_ENV', 'production')
    app.config.from_object(config_by_name[config_name])

    if not app.config['TESTING']:
        app.mongo = PyMongo()
        app.mongo.init_app(app)
    else:
        app.mongo = MongoMockClient()

    jwt.init_app(app)
    marshmallow.init_app(app)
    swagger.init_app(app)

    # Register Blueprints (Routes)
    from .routes.user import user_bp
    from .routes.auth import auth_bp
    from .routes.category import category_bp
    from .routes.tag import tag_bp
    from .routes.post import post_bp

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(tag_bp, url_prefix='/tags')
    app.register_blueprint(post_bp, url_prefix='/posts')

    return app
