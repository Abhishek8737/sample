from flask import current_app

from ecom.datastore import db
from ecom.exceptions import ServiceUnavailableException


class StatusManager():
    @staticmethod
    def check_status():
        status = {
            'status': 'up',
            'database_connected': True,
            'cache_connected': True,
        }
        try:
            db.get_engine(current_app).execute('SELECT 1')
        except Exception as e:
            status['database_connected'] = False
            status['status'] = 'down'


        if status['status'] == 'down':
            raise ServiceUnavailableException(status)

        return status
