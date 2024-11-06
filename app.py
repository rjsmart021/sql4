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
   
