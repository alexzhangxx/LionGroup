# send "one to one" notification to certain subscriber
'''response = ses.send_email(
    Source="maggiezhaomajoreee@gmail.com",
    Destination={
        'ToAddresses': ["rz2390@columbia.edu"]
    },
    Message={
        'Subject': {
            'Data': "test1",
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': "test1111",
                'Charset': 'UTF-8'
            }
        }
    }
)'''

# send notification to all subscribers
'''response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:055370712479:SignUpNoti',
    Message='you have just created an event',
    Subject='event notification',
)'''

import boto3
sns = boto3.client(
    'sns',
    aws_access_key_id='AKIAJJYDESANU5YJLSNQ',
    aws_secret_access_key='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',
    # aws_session_token=SESSION_TOKEN,
)
ses = boto3.client(
    'ses',
    aws_access_key_id='AKIAJJYDESANU5YJLSNQ',
    aws_secret_access_key='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',
    # aws_session_token=SESSION_TOKEN,
)

import pymongo
import datetime
client = pymongo.MongoClient('ec2-54-172-172-28.compute-1.amazonaws.com', 27017)
#client = pymongo.MongoClient('localhost', 27017)
db1 = client.user
db2 = client.event
User= db1.user
Event= db2.event
ID= 0
EID= 0
ID2=0
EID2=0


def create_student(info):
    #global ID
    global ID2
    #ID = ID + 1
    ID2=User.count()+1
    dic = {
        'id': ID2,
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

    #subscribe to our web application
    response1 = sns.subscribe(
        TopicArn='arn:aws:sns:us-east-1:055370712479:SignUpNoti',
        Protocol='email',
        Endpoint=dic['email']
    )

    #verify ses service
    response2 = ses.verify_email_address(
        EmailAddress=dic['email']
    )

    return ID2

def update_student(info,student):
    User.update_one(
        {"id": info['id']},
        {
        "$set": {
            'nick_name': student['nick_name'],
            'avatar': student['avatar'],
            'email': student['email'],
            'password': student['password'],
            'followings': info['followings'],
            'introduction': student['introduction'],
            'create_event': info['create_event'],
            'join_event': info['join_event'],
            'followers': info['followers']
        }
        }
    )
    return info['id']

def create_event_db(info, user_id):
    #global EID
    global EID2
    #EID = EID + 1
    EID2 = Event.count()+1
    d= datetime.datetime.now()
    dic = {
        'id': EID2,
        #'event_id':info['event_id'],
        'image': info['image'],
        'starter': user_id,
        'type':info['type'],
        'content':info['content'],
        'person_limit':30,
        'start_year': info['startyear'],
        'start_month': info['startmonth'],
        'start_day': info['startday'],
        'start_hour': info['startday'],
        'end_year': info['endyear'],
        'end_month': info['endmonth'],
        'end_day': info['endday'],
        'end_hour': info['endhour'],
        'time_limit_flag':False,
        'person_limit_flag':False,
        'follower': None,
        'joined_flag':False
    }
    Event.insert(dic)
    return dic, EID2


def find_student(id):
    info= User.find_one({"id": id})
    return info

def find_name_student(name):
    info = User.find_one({"nick_name": name})
    return info

def get_event_from_db():
    d = datetime.datetime.now()
    for c in Event.find():
        #if(c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
        if (int(c['end_year']) * 10000 + int(c['end_month']) * 100 + int(c['end_day']) < d.year * 10000 + d.month * 100 + d.day):
            c['time_limit_flag'] = True
    content= Event.find({'person_limit_flag': False, 'time_limit_flag': False})
    return content

def all_study_event():
    d = datetime.datetime.now()
    for c in Event.find():
        #if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
        if (int(c['end_year']) * 10000 + int(c['end_month']) * 100 + int(
                c['end_day']) < d.year * 10000 + d.month * 100 + d.day):
            c['time_limit_flag'] = True
    context= Event.find({"type": 'study', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def all_eat_event():
    d = datetime.datetime.now()
    for c in Event.find():
        #if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
        if (int(c['end_year']) * 10000 + int(c['end_month']) * 100 + int(
                c['end_day']) < d.year * 10000 + d.month * 100 + d.day):
            c['time_limit_flag'] = True
    context = Event.find({"type": 'eat', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def all_home_event():
    d = datetime.datetime.now()
    for c in Event.find():
        #if (c['end_year'] * 10000 + c['end_month'] * 100 + c['end_day'] < d.year * 10000 + d.month * 100 + d.day):
        if (int(c['end_year']) * 10000 + int(c['end_month']) * 100 + int(
                c['end_day']) < d.year * 10000 + d.month * 100 + d.day):
            c['time_limit_flag'] = True
    context = Event.find({"type": 'home', "person_limit_flag": False, 'time_limit_flag': False})
    return context

def find_my_moment(info):
    follower= info['followers']
    return follower

def get_all_my_event(user_id):
    context= Event.find({'starter': user_id})
    return context

