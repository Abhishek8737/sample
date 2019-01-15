import uuid
from datetime import date, datetime
from enum import Enum

from ecom.datastore import db
from ecom.models.custom_datatypes import UUID


class Base(db.Model):
    __abstract__ = True

    id = db.Column(UUID, primary_key=True, default=uuid.uuid4)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    modified_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow)

    def serialize(self):
        rv = {}
        attributes = getattr(self, 'serializable')
        for attribute in attributes:
            if isinstance(getattr(self, attribute), datetime) or \
                    isinstance(getattr(self, attribute), date):
                datetime_attr_value = getattr(self, attribute)
                rv[attribute] = datetime_attr_value\
                    .isoformat().replace('T', ' ')
            elif isinstance(getattr(self, attribute), Enum):
                rv[attribute] = getattr(self, attribute).name
            else:
                rv[attribute] = getattr(self, attribute)

        return rv
