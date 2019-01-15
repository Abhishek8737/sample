from flask import g
from ecom.authentication import HTTPAuthentication


class NoAuthentication(HTTPAuthentication):

    def authenticate(self):
        g.is_no_auth = True

        return True

    def is_no_auth(request):
        allowed_endpoints = [
            'post__service-auth_v3_dh-handshake-1',
            'post__service-auth_v3_dh-handshake-2',
            'post_tokens',
            'get_plans',
            'get_status',
            'get_showplus',
            'post_subscriptions',
        ]
        access_string = request.method.lower() + request.path.replace('/', '_')
        if access_string in allowed_endpoints:
            return True
        #return True
        return False
