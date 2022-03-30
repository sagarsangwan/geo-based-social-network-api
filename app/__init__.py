from flask import Flask


def create_app():
    from .posts import routes
    app = Flask(__name__)
    app.register_blueprint(routes.posts_bp)

    # from .weather import routes
    # app.register
    return app
