import base64
import hashlib
import hmac
import json
import urllib.parse as url_parse

from flask import current_app


def sign_payload(payload, signing_key):
    signed_data = []
    if 'signed' in payload:
        keys = payload['signed'].split(',')
        for key in keys:
            signed_data.append((key, payload[key]))
    else:
        signed_data = payload
    signed_data = url_parse.urlencode(signed_data).encode()
    signing_key = signing_key.encode()
    h = hmac.new(signing_key, signed_data, hashlib.sha1)

    return base64.encodestring(h.digest()).strip().decode('utf-8')


def sign_query_params(query_params, signing_key):
    signing_key = signing_key.encode()
    if isinstance(query_params, str):
        query_params = query_params.encode()
    h = hmac.new(signing_key, query_params, hashlib.sha1)

    return base64.encodestring(h.digest()).strip().decode('utf-8')


def sign_sha512(payload_signature_str):
    m = hashlib.sha512()
    m.update(payload_signature_str.encode())
    h = m.hexdigest()

    return h


def create_signature(
        payload, signing_keys, detail_keys=[], timestamp=None,
        request_reference_id=None, add_timestamp_in_payload=False):
    payments_salt = current_app.config['PAYMENTS_SALT']
    payments_product_key = current_app.config['PAYMENTS_PRODUCT_KEY']
    payload_signature_str = payments_product_key + '|'
    for key in signing_keys:
        if key in payload:
            payload_signature_str += str(payload[key]) + '|'
        else:
            payload_signature_str += '|'

    for suborder in payload.get('suborders', []):
        for detail_key in detail_keys:
            payload_signature_str += str(suborder[detail_key]) + '|'

    payload_signature_str += payments_salt

    if request_reference_id is not None:
        payload_signature_str += '|' + request_reference_id

    if add_timestamp_in_payload is True:
        payload_signature_str += '|' + timestamp

    signature = sign_sha512(payload_signature_str)

    if timestamp is not None:
        signature += '|' + timestamp

    return signature


def validate_signature_for_payload(payload, signing_keys, client_signature):
    if 'payload' in payload:
        payload['payload_string'] = json.dumps(payload['payload'], separators=(',', ':'))
        payload['type'] = payload['payload']['type']
    server_signature = create_signature(payload, signing_keys)

    if server_signature == client_signature:
        return True

    return False
