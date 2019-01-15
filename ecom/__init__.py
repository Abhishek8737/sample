from flask import request, g
from flask import Flask
import logging
from ecom.datastore import db, migrate, redis_store
from ecom.api import ecom_api



def _init_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile('config.py')

    return app


def _init_db(app):
    db.init_app(app)
    migrate.init_app(app)
    if app.config['ENV'] == 'development':
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def _init_cache(app):
    redis_store.init_app(app)


def _init_routes(app):
    # Capturing Flask's default exception handler
    # This hack is because flask-restful is overriding exception handler
    # https://github.com/flask-restful/flask-restful/issues/280
    handle_exceptions = app.handle_exception
    handle_user_exception = app.handle_user_exception
    ecom_api.init_app(app)
    # Restoring Flask's default exception handler
    app.handle_exceptions = handle_exceptions
    app.handle_user_exception = handle_user_exception


app = _init_app()


__import__('ecom.models')
__import__('ecom.routes')



_init_db(app)
_init_cache(app)
_init_routes(app)
