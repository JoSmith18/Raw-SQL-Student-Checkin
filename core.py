import db


def get_list_ids():
    return [ids.id for ids in db.get_all_ids()]


def get_list_names():
    return [name.student_name for name in db.get_all_names()]


def get_list_birthdates():
    return [bdays.birthdate for bdays in db.get_all_bdays()]
