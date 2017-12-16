import datetime
import os
from flask import Flask, request, render_template, session, redirect
from flask_cors import CORS
from logic import create_student_l, login, all_alive_event, study_event, eat_event, home_event, create_event, \
    get_my_moment, get_my_own

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
application = Flask(__name__, template_folder=tmpl_dir)
CORS(application)

application.secret_key = 'super secret key'
application.config['SESSION_TYPE'] = 'filesystem'


def args2dict(request_args, args):
    res = {}
    for arg in args:
        res[arg] = request_args.form[arg]
    return res


@application.route('/')
def home_page():
    return render_template('login.html')


@application.route('/register/')
def register_page():
    return render_template('register.html')


@application.route('/user/create/', methods=['POST'])
def register_user():
    args = ["nick_name", "avatar", "email", "password",
            "introduction"]
    user = args2dict(request, args)
    new_user = create_student_l(user)
    new_user['_id'] = str(new_user['_id'])
    print(new_user)
    session['user'] = new_user

    return redirect('/user/')


@application.route('/user/')
def user_home_page():
    if session['user'] is not None:
        return render_template('user.html')

    else:
        return render_template('error.html')


@application.route('/user/login/', methods=['POST'])
def login_user():
    user_nick = request.form['nick_name']
    password = request.form['password']
    user = login(user_nick, password)
    user['_id'] = str(user['_id'])
    # user = {'user_id': 1, 'nick_name': 'jack',
    #       'avatar': 'https://pbs.twimg.com/profile_images/747403736293617664/5pPvHX0G_400x400.jpg',
    #       'email': 'russwest44@gmail.com', 'password': '123456', 'introduction': 'why'}
    if user is not None:
        session['user'] = user
        return redirect('/user/')

    else:
        return render_template('error.html')


@application.route('/user/update/', methods=['POST'])
def update_st():
    '''
    args = ['user_id', "nick_name", "avatar", "since", "email", "password",
            "introduction"]
    student = args2dict(request, args)
    if len(student['password']) <= 6:
        return render_template('error.html')
    update_student_l(student)
    user_id = request.form['user_id']
    password = request.form['password']
    student = login(user_id, password)
    session['user'] = student'''
    return redirect('/user/')


@application.route('/discover/', methods=['GET'])
def get_all_event():
    user_id = session['user']['id']
    context = all_alive_event(user_id)
    # context = [{'nick_name': 'Jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
    #            'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
    #            'content': 'I would like to see coco.'},
    #           {'nick_name': 'Song', 'time': '2017-12-21', 'type': 'home', 'email': '53463462@qq.com',
    #            'image': 'http://schillyconstructioninc.com/wp-content/uploads/2017/08/home.jpg',
    #            'content': 'Go home together?'},
    #           {'nick_name': 'Yang', 'time': '2017-12-1', 'type': 'eat', 'email': '464753462@qq.com',
    #            'image': 'https://img.huffingtonpost.com/asset/585be1aa1600002400bdf2a6.jpeg?ops=scalefit_970_noupscale',
    #            'content': 'Eat nearby!'}
    #           ]
    return render_template('discover.html', events=context)


@application.route('/discover/join/', methods=['POST'])
def join_event():
    # event_id=request.form().....
    return redirect('/discover/')


@application.route('/discover/study/', methods=['GET'])
def get_study_event():
    user_id = session['user']['id']
    context = study_event(user_id)
    # context = [{'nick_name': 'Jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
    #            'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
    #            'content': 'I would like to see coco.'}]
    return render_template('discover.html', events=context)


@application.route('/discover/eat/', methods=['GET'])
def get_eat_event():
    user_id = session['user']['id']
    context = eat_event(user_id)
    # context = [{'nick_name': 'Yang', 'time': '2017-12-1', 'type': 'eat', 'email': '464753462@qq.com',
    #            'image': 'https://img.huffingtonpost.com/asset/585be1aa1600002400bdf2a6.jpeg?ops=scalefit_970_noupscale',
    #            'content': 'Eat nearby!'}]
    return render_template('discover.html', events=context)


@application.route('/discover/home/', methods=['GET'])
def get_home_event():
    user_id = session['user']['id']
    context = home_event(user_id)
    # context = [{'nick_name': 'Song', 'time': '2017-12-21', 'type': 'home', 'email': '53463462@qq.com',
    #            'image': 'http://schillyconstructioninc.com/wp-content/uploads/2017/08/home.jpg',
    #            'content': 'Go home together?'}]
    return render_template('discover.html', events=context)


@application.route('/myevent/start/', methods=['GET'])
def get_my_own_event():
    user_id = session['user']['id']
    context = get_my_own(user_id)

    # context = dict(moments=moments)
    # context = [{'nick_name': 'Jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
    #            'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
    #            'content': 'I would like to see coco.'}
    #           ]
    return render_template('myevent.html', events=context)


@application.route('/myevent/join/', methods=['GET'])
def get_my_join_event():
    user_id = session['user']['user_id']
    # moments = get_my_moment(user_id)
    # context = dict(moments=moments)
    context = [{'nick_name': 'Jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
                'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
                'content': 'I would like to see coco.'}
               ]
    return render_template('myevent.html', events=context)


@application.route('/event/create/', methods=['POST'])
def event_create():
    args = ["content", "image", "type"]
    trend = args2dict(request, args)
    d = datetime.datetime.now()
    user_id = session['user']['id']
    dic, EID = create_event(trend, user_id)
    # if session['user']['create_event'] is None:
    #    list=[]
    #    list.append(EID)
    #    session['user']['create_event']= list
    # else:
    #    session['user']['create_event'].append(EID)
    # create_trend_l(trend)
    t = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
    dic2 = {
        'nick_name': session['user']['nick_name'],
        'time': t,
        'type': dic['type'],
        'email': session['user']['email'],
        'image': dic['image'],
        'content': dic['content']
    }
    context = []
    context.append(dic2)
    return render_template('myevent.html', events=context)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):
        """
        This function handles command line parameters.
        Run the server using:
            python server.py
        Show the help text using:
            python server.py --help
        """

        HOST, PORT = host, port
        application.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


    run()
