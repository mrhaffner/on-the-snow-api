from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    with app.app_context():
        db.init_app(app)
        db.Model.metadata.reflect(db.engine)



def register_blueprints(app):
    from project.routes import blueprint

    app.register_blueprint(blueprint)
