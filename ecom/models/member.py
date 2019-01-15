from ecom.constants import Gender
from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class Member(Base):
    __tablename__ = 'subscription_members'
    subscription_id = db.Column(
        UUID, db.ForeignKey('subscriptions.id'), nullable=False)
    subscription = db.relationship(
        'Subscription', backref=db.backref('members'))
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(20), index=True)
    email = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))


    serializable = [
        'id', 'subscription_id', 'name',
        'mobile', 'email', 'age', 'gender', 'created_at', 'modified_at'
    ]

    def serialize(self):
        rv = super(Member, self).serialize()
        return rv
