from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

cars = [
  { 'id': 1, 'brand': 'Toyota', 'year': 2021, 'type': 'Coupe', 'color': 'Red'},
  { 'id': 2, 'brand': 'Lexus', 'year': 2012, 'type': 'Sedan', 'color': 'Blue'},
  { 'id': 3, 'brand': 'Range Rover', 'year': 2018, 'type': 'SUV', 'color': 'Brown'},
]

@app.route('/cars')
def cars_index():
  return jsonify(cars)

@app.route('/cars/<car_id>')
def cars_show(car_id):

  for car in cars:
    if car['id'] == int(car_id):
      return car
  return { 'error': 'Not Found' }, 404

@app.route('/cars', methods=['POST'])
def cars_create():
  new_car = request.get_json()
  new_car ['id'] = len(cars) + 1
  cars.append(new_car)
  return {'message': 'I love cars!'}, 201

app.run()