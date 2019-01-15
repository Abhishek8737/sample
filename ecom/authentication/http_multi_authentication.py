from functools import wraps

from flask import request

from ecom.authentication import (HTTPAuthentication, NoAuthentication)


class MultiAuthentication(HTTPAuthentication):
    def __init__(self, *auths):
        self.auths = auths
    def login_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            selected_auth = None
            request_scheme = None
            if NoAuthentication.is_no_auth(request):
                request_scheme = 'NoAuthentication'
                selected_auth = NoAuthentication()
            elif 'X-AUTH-SIGNATURE' in request.headers \
                    or (request.json and 'signature' in request.json) \
                    or (request.form and 'signature' in request.form):
                request_scheme = 'InterServiceAuthV2'
                selected_auth = HTTPInterServiceAuthV2()


            access_string = request.method.lower() + request.path.replace('/', '_')
            user_agent = request.headers.get('User-Agent')
            if user_agent and 'ios' in user_agent.lower():
                print('request.headers')
                print(request.headers)


            return selected_auth.login_required(f)(*args, **kwargs)

        return decorated
