import os

PROJECT_ROOT = os.getcwd()


class Config(object):
    # Database Setup
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(PROJECT_ROOT, 'dev_database.db'))


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(PROJECT_ROOT, 'prod_database.db'))
