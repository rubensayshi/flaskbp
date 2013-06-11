import logging
import os
from flaskbp.config import LazyConfigValue


class Config(object):
    """Base config to work from"""
    BASIC_LOG_LEVEL = logging.WARNING
    LOGGING_LEVEL = logging.WARNING
    EMAIL_LOGGING = False

    DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    VERSION_ON_DEV = False
    MAIN_VERSION   = None
    STATIC_VERSION = None
    APP_VERSION    = None
    VERSION_STRING_LENGTH = 10
    
    SECRET_KEY = '63fe3db58d1e3aa76432b6badbcafaeb'
    SESSION_COOKIE_NAME = "c_ses"
    SITE_NAME = 'FlaskBP'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 86400 * 60 # 60 days

    LOCALE_DEFAULT = 'nl_NL'
    
    BASE_APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    TMP_DIR = os.path.join(ROOT_DIR, "tmp")
     
    STATIC_DIR = os.path.join(BASE_APP_DIR, "static")
    
    FALLBACK_SERVER_NAME = 'localhost'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost/flaskbp?charset=utf8'
    SQLALCHEMY_POOL_RECYCLE = 600
    DATABASE_CONNECT_OPTIONS = {}
    
    REDIS_SERVER = 'localhost'
    REDIS_PORT   = 6379
    REDIS_DB     = 0
    REDIS_URL    = LazyConfigValue('redis://%(REDIS_SERVER)s:%(REDIS_PORT)d/%(REDIS_DB)d')
    
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "63fe3db58d1e3aa76432b6badbcafaeb"


class DevelopmentConfig(Config):
    pass

