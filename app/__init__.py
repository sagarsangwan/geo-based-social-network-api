import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = Flask(__name__)
    from .posts import routes as posts_routes
    app.register_blueprint(posts_routes.posts_bp)

    return app


app = create_app()


def database_connection(app):
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate(app, db)
    return db


database_connection = database_connection(app)
