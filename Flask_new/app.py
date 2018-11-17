from flask import Flask, render_template, jsonify, request
from flask.views import MethodView
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

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

news = [
    {
        'title': 'news_1',
        'text': "Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry",

    },
    {

        'title': 'news_2',
        'text': "Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry",

    }
]


class Cars(MethodView):
    Є

    def get(self, car_id):

        if car_id is None:
            return render_template('products.html', cars=cars)
        else:
            return render_template('details.html', some_car=list(filter(lambda x: x["id"] == car_id, cars)))

    def post(self):
        json_data = json.loads(request.data.decode('utf-8'))

        car = {
            "id": cars[-1]["id"] + 1,
            "model": json_data["model"],
            "description": json_data["description"]
        }
        cars.append(car)
        return jsonify(cars)

    def delete(self, car_id:int):
        for i, car in enumerate(cars):
            if car["id"] == car_id:
                del cars[i]
        return jsonify(cars)


car_view = Cars.as_view('car_api')
app.add_url_rule('/products', defaults={'car_id': None}, view_func=car_view, methods=['GET'])
app.add_url_rule('/products/<int:car_id>', view_func=car_view, methods=['GET', 'DELETE'])
app.add_url_rule('/products', view_func=car_view, methods=['POST'])


@app.route('/')
def home_page():
    return render_template('home.html', news=news)

