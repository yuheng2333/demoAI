from flask import Flask
from src.config import config
from flask_admin import Admin
from src.apps.translate.views import translate
from src.apps.llm.views import llm
from src.apps.api.views import api
# from src.apps.translate


def create_app(app_config=config):
    app = Flask(__name__, static_url_path='', static_folder="dist", template_folder="dist")
    app.config.from_object(app_config)

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return 'Welcome to visit demoAI'

    return app


def register_extensions(app):
    admin = Admin(app)


def register_blueprints(app):
    app.register_blueprint(translate, url_prefix='/translate')
    app.register_blueprint(llm, url_prefix='/llm')
    app.register_blueprint(api, url_prefix='/api')


def app_init(app):
    pass

