import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# administrator list
ADMINS = ['your-gmail-username@gmail.com']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    S3_BUCKET = os.environ['S3_BUCKET_NAME']
    S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
    S3_KEY = os.environ['S3_ACCESS_KEY']
    S3_SECRET = os.environ['S3_SECRET_ACCESS_KEY']



class TestingConfig(Config):
    TESTING = True
