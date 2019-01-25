import datetime
import uuid

from flask import g

from ecom.datastore import db
from ecom.exceptions import Unauthorized, ValidationError
from ecom.models import Member, Subscription


class SubscriptionManager():
    @classmethod
    def load(cls, id):
        return Subscription.query.filter_by(id=id).first()

    @classmethod
    def create_subscription(cls, user_data):
        print ("in create subscription")
        print (user_data)
        # Create subscription
        subscription = Subscription()
        subscription.start_date = datetime.date.today()
        subscription.end_date = datetime.date.today() + datetime.timedelta(days=365)


        primary_member = Member()
        primary_member.subscription = subscription
        primary_member.name = user_data.get('name')
        primary_member.mobile = user_data.get('mobile')
        primary_member.email = user_data.get('email')
        primary_member.age = user_data.get('age')
        primary_member.gender = user_data.get('gender')



        try:
            db.session.add(subscription)
            db.session.add(primary_member)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return [subscription, primary_member]

