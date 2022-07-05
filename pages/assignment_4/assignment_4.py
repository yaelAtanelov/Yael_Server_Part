from flask import Blueprint, render_template
from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

assignment_4 = Blueprint('assignment_4', __name__,
                  static_folder='static',
                  template_folder='templates')

@assignment_4.route('/assignment_4')
def users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


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



@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    email = request.form['user_email']
    for user in users_list:
        if email == user.Email:
            print(email)
            return render_template('assignment_4.html', registration_message='The user exists in the system!', users=users_list)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    fav_song = request.form['fav_song']
    query = "INSERT INTO users(first_name, last_name, email, password, fav_song) VALUES ('%s','%s','%s','%s','%s')" % (first_name, last_name, email, password, fav_song)
    print(f' {first_name} {last_name} {password}')
    interact_db(query=query, query_type='commit')
    return redirect('/assignment_4')


@assignment_4.route("/validation_user", methods=['POST'])
def validation_user():
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    email = request.form['user_email']
    password = request.form['password']
    for user in users_list:
        if email == user.Email:
            if password == user.password:
                user_id = user.id
                print(user_id)
                return render_template('assignment_4.html', v_id=user_id, users=users_list)
            else:
                return render_template('assignment_4.html', validation_message="Wrong password!", users=users_list)

    return render_template('assignment_4.html', validation_message="User not found!!", users=users_list)


@assignment_4.route("/update_email", methods=['POST'])
def update_email():
    user_id = request.form['user_id']
    email = request.form['email']
    query = "UPDATE users \
            SET Email= '%s' \
            WHERE id= '%s';" % (email, user_id)
    interact_db(query=query, query_type='commit')
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    return render_template('assignment_4.html', validation_message="Email changed successfully!", users=users_list)

@assignment_4.route("/update_password", methods=['POST'])
def update_password():
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    user_id = request.form['user_id']
    password1 = request.form['password1']
    password2 = request.form['password2']
    if password1 == password2:
        query = "UPDATE users \
                    SET password= '%s' \
                    WHERE id= '%s';" % (password1, user_id)
        interact_db(query=query, query_type='commit')
        return render_template('assignment_4.html', validation_message="Password changed successfully!", users=users_list)
    return render_template('assignment_4.html', validation_message="The passwords are not the same, please try again.", users=users_list)


@assignment_4.route("/update_song", methods=['POST'])
def update_song():
    user_id = request.form['user_id']
    song = request.form['song']
    query = "UPDATE users \
            SET fav_song= '%s' \
            WHERE id= '%s';" % (song, user_id)
    interact_db(query=query, query_type='commit')
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    return render_template('assignment_4.html', validation_message="Your favorite song has been updated!", users=users_list)



@assignment_4.route("/delete_user", methods=['POST'])
def delete_user():
    data = 'select * from users'
    users_list = interact_db(data, query_type='fetch')
    email = request.form['user_email']
    password = request.form['password']
    for user in users_list:
        if email == user.Email:
            if password == user.password:
                query = "DELETE FROM users WHERE email= '%s';" % email
                interact_db(query, query_type='commit')
                return redirect('/assignment_4')
            else:
                return render_template('assignment_4.html', Deletion_message="Wrong password!", users=users_list)

    return render_template('assignment_4.html', Deletion_message="User not found!!", users=users_list)







