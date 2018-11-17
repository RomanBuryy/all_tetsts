from flask import Flask, render_template, jsonify, request, Blueprint
from flask.views import MethodView
import json

cars = [
    {
        'id': 1,
        'model': 'Mersedes CLK 500',
        'description': 'Color - white',
    },
    {
        'id': 2,
        'model': 'KIA Sorento',
        'description': 'Color - black',
    }
]

class CarsView(MethodView):
    def get(self, car_id):
        if car_id is None:
            return render_template('products.html', cars=cars)
        else:
            return render_template('details.html', some_car=list(filter(lambda x: x["id"] == car_id, cars)))



api = Blueprint("api", __name__, template_folder="./templates")
api.add_url_rule("/products", defaults={'car_id': None}, view_func=CarsView.as_view("car_api"))
api.add_url_rule('/products/<int:car_id>', view_func=CarsView.as_view("car_api_2"))

