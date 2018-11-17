from flask import Flask, jsonify, render_template, url_for, request, redirect, session, flash, escape
import json
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')


@app.route('/products', methods=['GET'])
def create_list_products():
    return render_template('products.html', cars=cars)


@app.route('/products/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = do_get(car_id)
    return render_template('car_detail.html', car=car)


@app.route('/products/<int:car_id>', methods=['DELETE'])
def deleteOne(car_id):
    for i, q in enumerate(cars):
        if q['id'] == car_id:
            del cars[i]
    return jsonify(cars)


@app.route('/products', methods=['POST'])
def add_car():
    params = json.loads(request.data.decode('utf-8'))

    car = {
        "id": cars[-1]['id'] + 1,
        'model': params["model"],
        'description': params["description"],

    }
    cars.append(car)
    return jsonify(cars)


@app.errorhandler(404)
def error_404(error):
    return render_template("error404.html")


def do_get(id):
    car = list(filter(lambda c: c["id"] == id, cars))
    return car[0]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home_page'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home_page'))



if __name__ == '__main__':
    app.run(debug=True)
