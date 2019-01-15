from flask_restful import Resource

from ecom.authentication import authenticator
from ecom.authorization.acl import acl


class BaseController(Resource):
    """BaseController for decorating view methods"""
    decorators = [acl, authenticator.login_required]
