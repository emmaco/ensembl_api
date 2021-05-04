from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """
    Initialise the Flask application
    :rtype: Flask object
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        _init_errorhandlers(app)
        _init_blueprints(app)

        return app


def _init_blueprints(app):
    """
    Initialise the Flask blueprints
    :param app: flask app
    :type app: Flask object
    """
    from .home import home
    from .gene_queries import gene_queries

    app.register_blueprint(home.home_bp)
    app.register_blueprint(gene_queries.gene_query_bp)


def _init_errorhandlers(app):
    """
    Initialise error handlers
    :param app: flask app
    :type app: Flask object
    """
    from .errors import error_handlers
    app.register_blueprint(error_handlers.error_handlers_bp)
