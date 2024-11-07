from flask import Flask
from .extentions import init_extensions
from .views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    db_uri = 'mysql+pymysql://root:unodostres123@localhost/flask_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_extensions(app)
    return app
    