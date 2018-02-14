import db


def testCount():

    db.addStudents("Jo", '1999-01-18')

    amount = db.countStudents()

    db.deleteStudent("Jo")

    assert amount == 1
