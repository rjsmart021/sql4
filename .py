import psycopg2
import configparser
import pandas as pd
from sql_queries import*
import mysql.connector

#Connect to default database
conn = psycopg2.connect("host=127.0.0.1 dbname={} user={} password={}".format(DB_NAME_DEFAULT,DB_USER,DB_PASSWORD))
conn.set_session(autocommit=True)
cur = conn.cursor
#Add SQL Database
cur.execute("""CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);""")
conn.commit()
cur.execute("""CREATE TABLE WorkoutSessions (
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
    cur.execute("""INSERT INTO WorkoutSessions member_id, date, duration_minutes, calories_burned)
                    VALUES(%s,%s,%s,%s,%s,%d)""", row.tolist())
    conn.commit()

def add_member(member_id,First_Name, Last_Name,age, Gender):
    cur.execute("""INSERT INTO member_id,First_Name, Last_Name,age, Gender)
                    VALUES(%s,%s,%s,%s,%s,%d)""", row.tolist())
    conn.commit()
    
def update_member_age(member_id, new_age):
    cur.execute( """UPDATE WorkoutSessions SET age = 'new_age' WHERE member_id = '234';""")
    conn.commit()

 # Example code structure
def delete_workout_session(session_id):
    sql = """DELETE FROM WorkoutSessions WHERE name = 'session_id'"""
    cur.excecute(sql)
    conn.commit()
    

 def get_members_in_age_range(start_age, end_age):
    cur.execute("""SELECT * FROM Members WHERE Members BETWEEN 'start_age' AND 'end_age''""")
    conn.commit()
    %sql SELECT * FROM Members WHERE end_age ='40'


#Test 1
add_member(Sz678, Fitzgera, Kangory, 24, Male)
add_workout_session(Sz678,10/20/2024,70min,130)
update_member_age(Sz678,67)
delete_workout_session(554567)
get_members_in_age_range((45, 55)
