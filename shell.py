import db
import core


def add_student():
    name = input("What is the new student name?\n")
    birthdate = input(
        "What is {} birthdate? Format: yyyy/mm/dd\n".format(name))
    db.addStudents(name, birthdate)
    id = db.get_student_id(name, birthdate)
    print("Remember This ID YOU WILL NEED IT!!! ID={}".format(
        db.get_student_id(name, birthdate)))


def sign_in():
    id = input("What is your student ID??\n")
    if int(id) in core.get_list_ids():
        db.student_signin(id)
        print("Success!! You Made it here " +
              db.get_student_arrival(id).rfc2822())
    else:
        print("Incorrect Id You Must Start Over!!")


def get_id():
    name = input("What is your name student?-")
    birthdate = input("\nWhat is your birthdate? yyyy-mm-dd: ")
    if name in db.get_all_names() and birthdate in db.get_all_bdays():
        print("This is your id " + db.get_student_id(name, birthdate) +
              " now you will have to start over for forgetting!!")
    else:
        print(
            "That name and or birthdate is not in our system please start over and try again!!"
        )


def delete_student():
    print("****WARNING CANNOT UNDELETE STUDENT****")
    name = input("What is the name of the soon to be deleted student??->")
    if name in core.get_list_names():
        db.deleteStudent(name)
        print("The Delete Was Successful!!!")
    else:
        print("That name was not in the system restart and try again!!!")


def see_students():
    print("BCCA Students\n-------------")
    for student_name in core.get_list_names():
        print(student_name)


def get_times():
    id = input("What is the id of the student you would like to see?->")
    if int(id) in core.get_list_ids():
        print("Arrival Times\n-----------")
        for times in db.get_all_student_arrivals(id):
            print(times.rfc2822())
    else:
        print("ID not found restart and try again!!")


def main():
    first_choice = input("""Welcome To The Student Database!!\n\n
        To add Student Press 1 and Then Press Enter-\n\n
        To SignIn Press 2 and Then Press Enter-\n\n
        For Other Options Press 3 and Then Press Enter-\n""")

    if first_choice == "1":
        print("You have choosen to add a student......\n")
        add_student()
    elif first_choice == "2":
        print("You have choosen to signin.......\n")
        second_choice = input(
            "\nBefore We Go Further Do You Remember Your Student ID?? y or n -"
        )
        if second_choice.upper() == "y".upper():
            sign_in()
        elif second_choice.upper() == "n".upper():
            get_id()
        else:
            print("A mistake was made you will have to start over!!")
    elif first_choice == "3":
        third_choice = input("""Other Choices Are:\n\t
        1) Delete Student\n
        2) Get All Student Names\n
        3) Get All Check In Times(For Specific Student * Must Know ID)\n
        """)
        if third_choice == "1":
            print("You have choosen to delete a student......\n")
            delete_student()
        elif third_choice == "2":
            print("You have choosen to see all the students names......\n")
            see_students()
        elif third_choice == "3":
            print("You have choosen to see a student checkin times......\n")
            get_times()
    else:
        print("A mistake was made you will have to start over!!")


if __name__ == '__main__':
    main()