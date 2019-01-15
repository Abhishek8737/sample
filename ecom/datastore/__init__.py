from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis

db = SQLAlchemy()
migrate = Migrate(db=db, directory='ecom/migrations')
redis_store = FlaskRedis()
