from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector
import requests


app = Flask(__name__)


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

from pages.assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/assignment_4')

@app.route('/session')
def session_func():
    return jsonify(dict(session))

# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='bd121212',
                                         database='my_flask_db')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# ------------------------------------------------- #
# ------------------------------------------------- #


@app.route('/assignment4/users')
def assignment4_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return_list = []
    for user in users_list:
        user_dict = {
                       'first_name': user.first_name,
                       'last_name': user.last_name,
                       'Email': user.Email,
                       'fav_song': user.fav_song
                       }
        return_list.append(user_dict)
    return jsonify(return_list)


@app.route('/assignment4/outer_source')
def outer_source():
    print("outer_source")
    return render_template('outer_source.html')



@app.route('/fetch_be')
def fetch_be():
    if 'type' in request.args:
        print('after click')
        user_id = request.args['user_id']
        users = []
        res = requests.get('https://reqres.in/api/users/' +user_id)
        users.append(res.json())

        user_dict= {
            'first_name': users[0]['data']['first_name'],
            'last_name': users[0]['data']['last_name'],
            'email': users[0]['data']['email'],
            'avatar': users[0]['data']['avatar'],
        }

    return render_template('outer_source.html', first_name=user_dict['first_name'],
                           last_name=user_dict['last_name'],
                           email=user_dict['email'],
                           avatar=user_dict['avatar'])




@app.route('/assignment4/restapi_users', defaults={'USER_ID': 3})
@app.route('/assignment4/restapi_users/<int:USER_ID>')
def restapi_users(USER_ID):
    query = f'select * from users where id={USER_ID}'
    users_list = interact_db(query, query_type='fetch')

    if len(users_list) ==0:
        return_dict= {
            'message': f'user {USER_ID} not found'
        }
    else:
        users_list = users_list[0]
        return_dict = {'first_name': users_list.first_name,
                       'last_name': users_list.last_name,
                       'email': users_list.Email,
                       'fav_song': users_list.fav_song}
    return jsonify(return_dict)

if __name__ == '__main__':
    app.run(debug=True)
