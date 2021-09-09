import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

db = SQLAlchemy()
# migrate = Migrate()


def create_app(config_type):
    app = Flask(__name__)
    db_uri = os.environ.get('DB_URI')
    secret_key = os.environ.get('SECRET_KEY')
    app.config.update(
        TESTING=True,
        SECRET_KEY= secret_key,
        SQLALCHEMY_DATABASE_URI=db_uri
    )


    db.init_app(app)
    # migrate.init_app(app, db)

    from app.catalog import main
    app.register_blueprint(main)

    return app



