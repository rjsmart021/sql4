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
