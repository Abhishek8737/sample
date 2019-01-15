from functools import wraps

from flask import make_response, request


class HTTPAuthentication(object):
    """Authentication layer
    """
    def login_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not self.authenticate():
                # Clear TCP receive buffer of any pending data
                print ("not authorized")
            return f(*args, **kwargs)
        return decorated
