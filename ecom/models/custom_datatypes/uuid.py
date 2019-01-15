import uuid

from sqlalchemy import types


class UUID(types.TypeDecorator):
    impl = types.String

    def __init__(self, length=36):
        self.impl.length = length
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value and isinstance(value, uuid.UUID):
            return value
        elif value and not isinstance(value, uuid.UUID):
            return uuid.UUID(value)
        else:
            return None

    def process_result_value(self, value, dialect=None):
        if value:
            return value
        else:
            return None
