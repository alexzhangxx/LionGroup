import pymongo
client = pymongo.MongoClient('localhost', 27017)
db1 = client.user
db2 = client.event
User= db1.user
Event= db2.event
ID= 1

def create_student(info):
    global ID
    ID = ID + 1
    dic = {
        'id': ID,
        'nick_name': info['nick_name'],
        'avatar': info['avatar'],
        'email': info['email'],
        'password': info['password'],
        'followers': None,
        'followings': None,
        'introduction': info['introduction']
    }
    User.insert(dic)
    return ID


def find_student(id):
    info= User.find_one({"id": id})
    return info

def find_name_student(name):
    info = User.find_one({"nick_name": name})
    return info


def find_my_moment(info):
    follower= info[followers]
