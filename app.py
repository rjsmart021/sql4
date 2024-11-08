from flask import Flask, request, jsonify

app = Flask(__name__)

members = [
    {"id": 1, "name": "Margarette", "phone_Number": 75434878765, "email": "Md@gmail.com"},
    {"id": 2, "name": "Suzan", "phone_Number": 9543066556, "email": "S2@gmail.com"},
    {"id": 3, "name": "Egypt", "phone_Number": 30556765456, "email": "Egp@gmail.com"},
]

def _find_next_id():
    return max(member["id"] for member in members) + 1

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    return jsonify(member)

@app.route('/members/add_member', methods=['POST'])
def add_member():
    if request.is_json:
        member = request.get_json()
        member["id"] = _find_next_id()
        members.append(member)
        return member, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/members', methods=['UPDATE'])
def update_member(id):
    if request.is_json:
        member = request.get_json()
        return jsonify(member)
        member["id"] = _find_next_id()
        members.append(member)

@app.route('/members', methods=['DELETE'])
def delete_member(id):
    if request.is_json:
        member = request.get_json()
        member["id"] = _find_next_id()
        members.delete(member)
class Members(db.Model):
    def __init__(self, member_id, member_name, phone_number, email, Active=True):
        self.member_id = member_id
        self.member_name = member_name
        self.phone_number = phone_number
        self.email = email
        self.Active = Active

class Workouts(db.Model):
    def __init__(self, workout_activity, workout_time, workout_rating, members_inworkout):
        self.workout_id = workout_id
        self.workout_activity = workout_activity
        self.workout_time = workout_time
        self.workout_rating = workout_rating
        self.members_inworkout = []
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from API_MINI import app
ma = Marshmallow()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Bakery as BakeryModel, Product as productModel, product_genres, db
from sqlalchemy.orm import Session
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(workout_id):
    return jsonify(workout)

@app.route('/workouts/add_workout', methods=['POST'])
def add_workout():
    if request.is_json:
        workout = request.get_json()
        workout["workout_id"] = 
        workouts.append(workout)
        return workout, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/workouts', methods=['UPDATE'])
def update_workout(id):
    if request.is_json:
        member = request.get_json()
        return jsonify(member)
        member["workout_id"] = a
        members.append(workout)

@app.route('/members', methods=['DELETE'])
def delete_workout(id):
    if request.is_json:
        member = request.get_json()
        member["id"] = _find_next_id()
        members.delete(member)
   
