from flask import current_app, g, request

from ecom.authentication import HTTPAuthentication
from ecom.exceptions import Unauthorized, ValidationError
from ecom.utils import signing_util


class HTTPInterServiceAuthV2(HTTPAuthentication):

    def get_auth(self):
        service = None
        if 'X-AUTH-SERVICE' in request.headers:
            service = request.headers['X-AUTH-SERVICE']
        elif request.json and 'service' in request.json:
            service = request.json['service']
        elif request.form and 'service' in request.form:
            service = request.form['service']
        if request.path == '/_app_logout':
            service = 'accounts'
        if not service:
            raise ValidationError('Service not found or empty')


        signature = None
        if 'X-AUTH-SIGNATURE' in request.headers:
            signature = request.headers['X-AUTH-SIGNATURE']
        elif request.json and 'signature' in request.json:
            signature = request.json['signature']
        elif request.form and 'signature' in request.form:
            signature = request.form['signature']
        if not signature:
            raise ValidationError('Signature not found or empty')

        return [signature, service]

    def authenticate(self):
        [client_signature, service] = self.get_auth()
        signing_key = current_app.config['SIGNING_KEYS'][service.upper()]
        if request.method == 'GET':
            server_signature = signing_util.sign_query_params(request.query_string, signing_key)
        else:
            if request.json:
                payload = request.json
            elif request.form:
                payload = request.form
            server_signature = signing_util.sign_payload(payload, signing_key)
        if server_signature == client_signature:
            g.service_name = service
            return True
        raise Unauthorized('Signature mismatch')

