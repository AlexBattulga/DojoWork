from flask import Flask, render_template, session, flash, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'thisIsMySecretKey'
mysql = MySQLConnector(app, 'friendsdatabase')

@app.route('/')
def users():                                                                    # Selecting data from database and passing to index.html
    users = mysql.query_db('SELECT CONCAT(first_name, " ", last_name) as full_name, id, email, created_at FROM friends')
    return render_template('index.html', all_users=users)

@app.route('/users/create')                                                     # Path to create_user.html
def create_path():
    return render_template('create_user.html')

@app.route('/users/new', methods=['POST'])                                      # Getting data from create_user.html form and inserting to friends table
def create():
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']

    query = 'INSERT INTO friends (first_name, last_name, email, created_at) \
    VALUES (:fname, :lname, :email, NOW())'
    data = {
        'fname': fname,
        'lname': lname,
        'email': email
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/users/<user_id>')                                                  # Showing user information based on their ID
def actions(user_id):
    query = 'SELECT * FROM friends WHERE id = :id'
    data = {
        'id':user_id
    }
    user = mysql.query_db(query, data)
    return render_template('show.html', users=user)

@app.route('/users/<user_id>/destroy')                                          # Deleting data from friends table by ID
def destroy(user_id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = {
        'id': user_id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/user/edit/<user_id>')                                              # Path to edit.html
def edit_path(user_id):
    UserId = user_id
    return render_template('edit.html', UserId=UserId)

@app.route('/users/edit/<user_id>', methods=['POST'])                           # Updating user information by their ID
def edit(user_id):
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']

    query = 'UPDATE friends SET first_name = :fname, last_name = :lname, \
    email = :email, created_at = NOW() WHERE id =:user'
    data = {
        'user': user_id,
        'fname': fname,
        'lname': lname,
        'email': email
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
