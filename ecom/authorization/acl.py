from functools import wraps

from flask import g, request

from ecom.exceptions import AccessDenied


def acl(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        access_string = request.method.lower() + '_' + request.endpoint
        access_allowed = None
        if 'is_no_auth' in g:
            access_allowed = True
        elif 'role_name' in g:
            if access_string in ACL_MAP[g.role_name]:
                access_allowed = True
        elif 'service_name' in g:
            service_name = g.service_name.upper()
            if service_name in ACL_MAP and \
                    access_string in ACL_MAP[service_name]:
                access_allowed = True
        if not access_allowed:
            raise AccessDenied('You are not authorized to use this resource')

        return f(*args, **kwargs)
    return decorated


ACL_MAP = {
    'USER': [
        'get_cities',
        'put_leads',
        'post_tokens',
    ],
    'DOSE': [
        'get__members',
    ],
    'ADMIN': [
        'get_plus',
        'get_dashboard_subscription_usage',
        'get_dashboard_transactions',
    ],
    'SUPERADMIN': [
        'get_plus',
        'get_dashboard_subscription_usage',
        'get_dashboard_transactions',
        'post_payment_credits',
        'delete_members_member_id',
    ],
    'PAYMENTS': [
        'post__payment_notification',
    ],
}
