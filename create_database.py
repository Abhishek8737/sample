from subscriptions import app
from sqlalchemy import create_engine
import time

db_name = app.config.get('DB_NAME')
user = app.config.get('DB_USER')
passwd = app.config.get('DB_PASSWORD')
host = app.config.get('DB_HOST')

def create_db(retry=0):
    try:
        mysql_engine = create_engine(
            'mysql://{}:{}@{}'.format(user, passwd, host)
        )
        result = mysql_engine.execute(
            'CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci'.format(db_name)
        )
        result.close()
    except Exception:
        if retry > 3:
            raise
        time.sleep(1)
        create_db(retry+1)

create_db()
