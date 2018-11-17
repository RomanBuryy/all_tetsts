from flask import Flask

from my_blueprint import api

app = Flask(__name__)

from my_blueprint.api.routes import mod

app.register_blueprint(api.routes.mod, url_prefix = '/')