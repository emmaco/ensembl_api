from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # create the application context
        # anything not here does not exist
        from .home import home
        from .gene_queries import gene_queries

        # register blueprints here
        app.register_blueprint(home.home_bp)
        app.register_blueprint(gene_queries.gene_query_bp)

        return app
