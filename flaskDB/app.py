from flask import Flask, render_template, jsonify, request, Blueprint
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roman:111@localhost/roman'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Car(db.Model):
    __tablename__ = "cars_table"
    id = db.Column(db.Integer, autoincrement = True ,primary_key=True)
    carname = db.Column(db.String(80), nullable=False)
    car_color = db.Column(db.String(120), nullable=False)

    def __init__(self, carname, car_color):
        # self.id = id
        self.carname = carname
        self.car_color = car_color

    def __repr__(self):
        return "<Car %r>" % self.carname
        


class Cars(MethodView):
    def get(self, id=''):
        if id:
            car = Car.query.filter_by(id=id).first()
            # return car_schema.jsonify(car)
            return render_template('details.html', car = car)
            
        else:
            car = Car.query.order_by(Car.id).all()
            # return users_schema.jsonify(user)
            return render_template('products.html', cars = car)
    
    def post(self):
        data_car = json.loads(request.data)
        model = request.form['add_car_model']
        color = request.form['add_car_color']
        new_car = Car(model, color)
        

        db.session.add(new_car)
        db.session.commit()
        return car_schema.jsonify(new_car)

    def put(self, id):
        data_user = json.loads(request.data)
        new_user_email = data_user["car_color"]

        user = Car.query.filter_by(id=id).first()
        user.car_color = new_user_email

        db.session.commit()
        return car_schema.jsonify(data_user)

    def delete(self, id):
        data_user = Car.query.filter_by(id=id).first()

        db.session.delete(data_user)
        db.session.commit()
        return car_schema.jsonify(data_user)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("carname", "car_color")

cars_schema = UserSchema(many=True)
car_schema = UserSchema()

car_view = Cars.as_view("car_api")
app.add_url_rule('/products', view_func=car_view, methods=['GET', 'POST'])
app.add_url_rule('/car/<int:id>', view_func=car_view, methods=['DELETE', 'GET', 'PUT'])


@app.route('/')
def home_page():
    return render_template('home.html')