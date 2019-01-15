from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class Subscription(Base):
    __tablename__ = 'subscriptions'
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


    serializable = ['id', 'start_date', 'end_date']

    def serialize(self):
        rv = super(Subscription, self).serialize()
        return rv
