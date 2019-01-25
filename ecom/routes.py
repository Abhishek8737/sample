from ecom.api import ecom_api
from ecom.controllers import *

ecom_api.add_resource(StatusController, '/status', methods=['GET'], endpoint='status')
ecom_api.add_resource(SubscriptionsController, '/subscriptions', methods=['GET', 'POST'], endpoint='subscriptions')
