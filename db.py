import records
import maya

db = records.Database('postgres:///signin')


def addStudents(name, birthdate):
    db.query(
        "INSERT INTO students (student_name, birthdate) VALUES (:name,:bday);",
        name=name,
        bday=birthdate)


def get_student_id(name, birthdate):
    student_id = db.query(
        """SELECT students.id FROM students 
    WHERE students.student_name = :name and students.birthdate = :bday;""",
        name=name,
        bday=birthdate)
    return student_id.first().id


def countStudents():
    amount = db.query(
        "SELECT count(student_name) as num FROM students;").first()
    return amount.num


def deleteStudent(name):
    db.query("DELETE FROM students WHERE student_name = :name", name=name)


def get_all_ids():
    ids = db.query("SELECT id FROM students;")
    return ids.all()


def get_all_names():
    names = db.query("SELECT student_name From students;")
    return names.all()


def get_all_bdays():
    bdays = db.query("SELECT birthdate FROM students;")
    return bdays.all()


def student_signin(student_id):
    db.query(
        "INSERT INTO signin (student_id) VALUES (:student_id);",
        student_id=student_id)


def get_student_arrival(student_id):
    timestamp = db.query(
        """SELECT arrival
        FROM signin
        WHERE :student_id = student_id
        order by arrival desc
        limit 1;""",
        student_id=student_id)
    return maya.MayaDT.from_datetime(timestamp.first().arrival)


def who_signed_in():
    student_here = db.query(
        "SELECT student_name FROM students,signin WHERE students.id = student_id;"
    )

    return student_here.all()


def get_all_student_arrivals(student_id):
    timestamp = db.query(
        """SELECT arrival
        FROM signin
        WHERE :student_id = student_id
        order by arrival desc""",
        student_id=student_id)
    return [maya.MayaDT.from_datetime(times.arrival) for times in timestamp]