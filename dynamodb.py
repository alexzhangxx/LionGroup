import pymongo
import datetime
client = pymongo.MongoClient('localhost', 27017)
db1 = client.user
db2 = client.event
User= db1.user
Event= db2.event
ID= 0
EID= 0

def create_student(info):
    global ID
    ID = ID + 1
    dic = {
        'id': ID,
        'nick_name': info['nick_name'],
        'avatar': info['avatar'],
        'email': info['email'],
        'password': info['password'],
        'followings': None,
        'introduction': info['introduction'],
        'create_event': None,
        'join_event': None,
        'followers':None
    }
    User.insert(dic)
    return ID

def create_event_db(info, user_id):
    global EID
    EID = EID + 1
    d= datetime.datetime.now()
    dic = {
        'id': EID,
        #'event_id':info['event_id'],
        'image': info['image'],
        'starter': user_id,
        'type':info['type'],
        'content':info['content'],
        'person_limit':30,
        'start_year': 2017,
        'start_month': 7,
        'start_day': 31,
        'start_hour': 11,
        'end_year': 2018,
        'end_month': 12,
        'end_day': 31,
        'end_hour': 12,
        'time_limit_flag':False,
        'person_limit_flag':False,
        'follower': None,
        'joined_flag':False
    }
    Event.insert(dic)
    return dic, EID


def find_student(id):
    info= User.find_one({"id": id})
    return info

def find_name_student(name):
    info = User.find_one({"nick_name": name})
    return info

def get_event_from_db():
    d = datetime.datetime.now()
    for c in Event.find():
        if(c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
            print(c)
            c['time_limit_flag'] = True
    content= Event.find({'person_limit_flag': False, 'time_limit_flag': False})
    return content

def all_study_event():
    d = datetime.datetime.now()
    for c in Event.find():
        if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
            print(c)
            c['time_limit_flag'] = True
    context= Event.find({"type": 'study', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def all_eat_event():
    d = datetime.datetime.now()
    for c in Event.find():
        if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
            print(c)
            c['time_limit_flag'] = True
    context = Event.find({"type": 'eat', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def all_home_event():
    d = datetime.datetime.now()
    for c in Event.find():
        if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
            print(c)
            c['time_limit_flag'] = True
    context = Event.find({"type": 'home', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def find_my_moment(info):
    follower= info['followers']
    return follower

def get_all_my_event(user_id):
    context= Event.find({'starter': user_id})
    return context

