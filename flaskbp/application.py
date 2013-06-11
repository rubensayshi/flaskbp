def create_app(full = True):
    from flask import Flask
    import sys
    sys.path.append('flaskbp')

    app = Flask(__name__)
    app.static_path = app.static_folder

    _setup_config(app)
    _setup_version(app)
    _setup_db(app)

    from flaskbp.view.jinja_helpers import setup_jinja_helpers
    setup_jinja_helpers(app)
    _setup_blueprints(app)
    _setup_clicontext(app)

    return app


def get_environment():
    import os
    """return the environment from an environment variable,
    should be development|test|staging|production"""
    return os.environ.get('ENVIRONMENT', 'development')


def _setup_version(app):
    from flaskbp.config import MAIN_VERSION, STATIC_VERSION, APP_VERSION

    app.config['MAIN_VERSION']   = MAIN_VERSION
    app.config['STATIC_VERSION'] = STATIC_VERSION
    app.config['APP_VERSION']    = APP_VERSION


def _setup_config(app):
    from flaskbp.config import config
    app.config.update(config)


def _setup_db(app):
    from flaskbp.models import db

    db.init_app(app)
    db.app = app
    app.db = db


def _setup_blueprints(app):
    from flaskbp.view.blueprints.main import main

    app.register_blueprint(main)


def _setup_clicontext(app):
    def get_cli_context(**kwargs):
        from flask import _request_ctx_stack
        
        # return the current request context if possible
        if _request_ctx_stack.top is not None:
            return _request_ctx_stack.top
        
        options = {'SERVER_NAME' : app.config['FALLBACK_SERVER_NAME'],
                   'SERVER_PORT' : '',
                   'REQUEST_METHOD' : 'GET',
                   'wsgi.url_scheme' : 'http'}
        options.update(kwargs or {})

        return app.request_context(options)

    app.cli_request_context = get_cli_context

