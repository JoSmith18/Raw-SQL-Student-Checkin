CREATE TABLE students (id Serial UNIQUE Primary Key, student_name Text, birthdate Date);

CREATE TABLE signin (id Serial UNIQUE PRIMARY KEY, 
student_id Integer references students (id), 
arrival Timestamp default Current_Timestamp );

