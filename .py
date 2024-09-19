import psycopg2
import configparser
import pandas as pd
from sql_queries import*

#Connect to default database
conn = psycopg2.connect("host=127.0.0.1 dbname={} user={} password={}".format(DB_NAME_DEFAULT,DB_USER,DB_PASSWORD))
conn.set_session(autocommit=True)
cur = conn.cursor
#Add SQL Database
cur.excecute("""CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);""")
conn.commit()
cur.excecute("""CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);""")
conn.commit()
#Close connction
conn.close()
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    cur.excecute("""INSERT INTO WorkoutSessions member_id, date, duration_minutes, calories_burned)
                    VALUES(%s,%s,%s,%s,%s,%d)""", row.tolist())
    conn.commit()

   
def update_member_age(member_id, new_age):
    cur.excecute( """UPDATE WorkoutSessions SET age = 'new_age' WHERE member_id = '234';""")
    conn.commit()

 # Example code structure
def delete_workout_session(session_id):
    sql = """DELETE FROM WorkoutSessions WHERE name = 'session_id'"""
    cur.excecute(sql)
    conn.commit()
    

 def get_members_in_age_range(start_age, end_age):
    cur.excecute("""SELECT * FROM Members WHERE Members BETWEEN 'start_age' AND 'end_age''""")
    conn.commit()
    %sql SELECT * FROM Members WHERE end_age ='40'
