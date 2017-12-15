import datetime
from dynamodb import create_student, find_student, find_name_student

def login(user_nick, password):
    user = find_name_student(user_nick)
    if user is not None and user['password'] == password:
        return user
    else:
        return None

def create_student_l(student):
    student['since'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    id= create_student(student)
    return find_student(id)

def get_my_moment(user_id):
    info= find_student(user_id)
    return find_my_moment(info)