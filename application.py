import os
from flask import Flask, request, render_template, session, redirect
from flask_cors import CORS

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
    # new_user = create_user_l(user)
    # session['user'] = new_user
    return redirect('/user/')


@application.route('/user/')
def user_home_page():
    if session['user'] is not None:
        return render_template('user.html')

    else:
        return render_template('error.html')


@application.route('/user/login/', methods=['POST'])
def login_user():
    user_id = request.form['user_id']
    password = request.form['password']
    # user = login(user_id, password)
    user = {'user_id': 1, 'nick_name': 'jack',
               'avatar': 'https://pbs.twimg.com/profile_images/747403736293617664/5pPvHX0G_400x400.jpg',
               'email': 'russwest44@gmail.com', 'password': '123456', 'introduction': 'why'}
    if user is not None:
        session['user'] = user
        return redirect('/user/')

    else:
        return render_template('error.html')


@application.route('/discover/', methods=['GET'])
def get_all_moment():
    user_id = session['user']['user_id']
    # moments = get_my_moment(user_id)
    # context = dict(moments=moments)
    context = [{'nick_name': 'jack', 'time': '2017-12-20', 'type': 'study', 'email': '1253263462@qq.com',
                'image': 'https://i.ytimg.com/vi/zNCz4mQzfEI/maxresdefault.jpg',
                'content': 'I would like to see coco.'}]
    return render_template('discover.html', events=context)


'''
@application.route('/trend/', methods=['GET'])
def my_trend():
    user_id = session['user']['user_id']
    trends = get_my_trend_l(user_id)
    my_circles = get_my_circle(user_id)
    context = dict(trends=trends, circles=my_circles)
    return render_template('trend.html', **context)


@application.route('/circle/', methods=['GET'])
def get_circle_school():
    user_id = session['user']['user_id']
    school_id = session['user']['school_id']
    circles = get_all_circle_l(user_id, school_id)
    context = dict(circles=circles)
    return render_template('circle.html', **context)
'''

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
