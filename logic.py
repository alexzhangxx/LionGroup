import datetime
from dynamodb import create_student, find_student, find_name_student, get_event_from_db, all_study_event, all_eat_event, all_home_event, create_event_db, find_my_moment, get_all_my_event

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

def all_alive_event(user_id):
    context= get_event_from_db()
    user = find_student(user_id)
    list = []
    for c in context:
        t = str(c['start_year']) + "-" + str(c['start_month']) + "-" + str(c['start_day'])
        dic = {
            'nick_name': user['nick_name'],
            'time': t,
            'type': c['type'],
            'email': user['email'],
            'image': c['image'],
            'content': c['content']
        }
        list.append(dic)
    return list

def study_event(user_id):
    context= all_study_event()
    user = find_student(user_id)
    list = []
    for c in context:
        t = str(c['start_year']) + "-" + str(c['start_month']) + "-" + str(c['start_day'])
        dic = {
            'nick_name': user['nick_name'],
            'time': t,
            'type': c['type'],
            'email': user['email'],
            'image': c['image'],
            'content': c['content']
        }
        list.append(dic)
    return list


def eat_event(user_id):
    context= all_eat_event()
    user = find_student(user_id)
    list = []
    for c in context:
        t = str(c['start_year']) + "-" + str(c['start_month']) + "-" + str(c['start_day'])
        dic = {
            'nick_name': user['nick_name'],
            'time': t,
            'type': c['type'],
            'email': user['email'],
            'image': c['image'],
            'content': c['content']
        }
        list.append(dic)
    return list

def home_event(user_id):
    context= all_home_event()
    user = find_student(user_id)
    list = []
    for c in context:
        t = str(c['start_year']) + "-" + str(c['start_month']) + "-" + str(c['start_day'])
        dic = {
            'nick_name': user['nick_name'],
            'time': t,
            'type': c['type'],
            'email': user['email'],
            'image': c['image'],
            'content': c['content']
        }
        list.append(dic)
    return list

def create_event(trend, user_id):
    return create_event_db(trend, user_id)

def get_my_moment(user_id):
    info= find_student(user_id)
    return find_my_moment(info)

def get_my_own(user_id):
    #context = [{'nick_name': 'Jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
    #            'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
    #            'content': 'I would like to see coco.'}
    #           ]
    context= get_all_my_event(user_id)
    user= find_student(user_id)
    list=[]
    for c in context:
        t = str(c['start_year']) + "-" + str(c['start_month']) + "-" + str(c['start_day'])
        dic = {
            'nick_name': user['nick_name'],
            'time': t,
            'type': c['type'],
            'email': user['email'],
            'image': c['image'],
            'content': c['content']
        }
        list.append(dic)
    return list






