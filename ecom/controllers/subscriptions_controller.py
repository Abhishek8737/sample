from flask import jsonify, request

from ecom.controllers import BaseController
from ecom.managers import SubscriptionManager


class SubscriptionsController(BaseController):
    def get(self):
        subscription_id = request.args.get('subscription_id',type=str)
        subscription = SubscriptionManager.load(id=subscription_id)
        serialized_subscriptions = []
        serialized_subscriptions.append(subscription.serialize())
        return jsonify(serialized_subscriptions)

    def post(self):
        x_profile_token = request.headers.get('X-PROFILE-TOKEN')
        subscription, primary_member = SubscriptionManager.create_subscription(request.json)
        return {
            'subscription': subscription.serialize(),
            'primary_member': primary_member.serialize(),
        }
