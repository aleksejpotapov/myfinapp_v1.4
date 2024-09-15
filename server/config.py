class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '68d5f4g65sdf4g654sdfg654'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'ru']
    CACHE_TYPE = 'simple'

    # flask-user configurations
    MAIL_SERVER='smtp-legacy.office365.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'info@myfinapp.me'
    MAIL_PASSWORD = 'Vinegret4me'
    MAIL_DEFAULT_SENDER = 'info@myfinapp.me'
    SECURITY_EMAIL_SENDER = 'info@myfinapp.me'
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    SCHEDULER_API_ENABLED = True

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    DEVELOPMENT = False
    DEBUG_TB_PROFILER_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://uaoo8llisgtjse:pdf4032b71929ba472e02516324b7362d2495fb8e8c7e1b60885bbcaa2b150732@ec2-54-78-213-96.eu-west-1.compute.amazonaws.com:5432/d8s1n6k0ofaonc'

class StagingConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'postgres://uaoo8llisgtjse:pdf4032b71929ba472e02516324b7362d2495fb8e8c7e1b60885bbcaa2b150732@ec2-54-78-213-96.eu-west-1.compute.amazonaws.com:5432/d8s1n6k0ofaonc'

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    pg_user = "postgres"
    pg_pwd = "EgorTitov9!"
    pg_port = "5432"
    pg_name = "myfinapp_local_1_3"
    DEBUG_TB_PROFILER_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost:{port}/{db_name}".format(username=pg_user, password=pg_pwd, port=pg_port, db_name=pg_name)
