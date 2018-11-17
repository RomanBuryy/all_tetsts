from flask import Flask, render_template, jsonify, request
from flask.views import MethodView
import json
from api import api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roman:roman@localhost/roman'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(api)
db = SQLAlchemy(app)








@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

