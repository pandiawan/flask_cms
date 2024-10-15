import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DEBUG = os.getenv("FLASK_DEBUG", default=False)
    SECRET_KEY = os.getenv("SECRET_KEY", default="secret_key")
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', default='jwt_secret_key')
    IMAGE_FOLDER = 'images'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongomock://localhost/test_db'  # Menggunakan mongomock untuk testing


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}