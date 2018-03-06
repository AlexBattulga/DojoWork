from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import MySQLConnector
import re
import md5
import time
app = Flask(__name__)
app.secret_key = 'iiuu#@#$%^&&*()'
mysql = MySQLConnector(app, 'the_wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation
NAME_REGEX = re.compile(r'^[^0-9]+$')                                      #string validation

@app.route('/')
def index():
    if "id" in session:                                                    #if id in session it will redirect to success.html
        return redirect('/wall')
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    hashed_password = md5.new(password).hexdigest()                        # hashed user password and confirm_password
    hashed_confirm_password = md5.new(confirm_password).hexdigest()

    error = False                                                          # Selecting email and username from database that equal to user input email and password
    main_query = 'SELECT * FROM users WHERE email = :email or first_name = :first_name'
    main_data = {
                'email': email,
                'first_name': first_name
    }
    validate =mysql.query_db(main_query, main_data)

    if len(validate) == 0:                                                 # Conditions
        if len(first_name) < 2:
            flash('Must enter more than 2 characters!')
        elif not NAME_REGEX.match(first_name):
            flash('Must enter characters!')

        if len(last_name) < 2:
            flash('Must enter more than 2 characters!')
        elif not NAME_REGEX.match(last_name):
            flash('Must enter characters!')

        if len(email) < 1:
            flash('You must enter an email address!')
        elif not EMAIL_REGEX.match(email):
            flash("Invalid email address.",'error')

        if len(password) < 1:
            flash('You must enter your password!')
            error = True
        elif len(password) < 8:
            flash('Password must be more than 8 characters!')
            error = True

        if confirm_password < 1:
            flash('You must enter your password agian!')
            error = True
        elif confirm_password != password:
            flash('Password did not match!')
            error = True
        if error:
            return redirect('/')
        else:                                                               # If everything is validated, data will be append into a table
            query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:f_name, :l_name, :user_email, :user_password, NOW(), NOW())'
            data = {
                    'f_name':first_name,
                    'l_name': last_name,
                    'user_email':email,
                    'user_password':hashed_password
            }
            mysql.query_db(query, data)
            flash('Your information successfully stored in our database. Please log in now!')
        return redirect('/')
    flash('This email address or Name is already exist!')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user_email = request.form['user_email']
    user_password = md5.new(request.form['user_password']).hexdigest()

    query = 'SELECT * FROM users WHERE email = :email Limit 1'
    data = {
            'email': user_email,
    }
    user = mysql.query_db(query, data)
    if len(user) > 0:
        user_data = user[0]
        if user_data['password'] == user_password:
            session["id"] = user_data["id"]
            return redirect('/wall')
        else:
            flash('Wrong password')
            return redirect('/')
    else:
        flash('email doesnt exist!')
        return redirect('/')
@app.route('/wall')
def success():
    if 'id' not in session:
        return redirect('/')
    #logged in user
    query1 = 'SELECT * FROM users WHERE id = :user_id'
    data1 = {
        'user_id': session['id']
    }
    user_id = mysql.query_db(query1, data1)

    messages = mysql.query_db('SELECT CONCAT(first_name, " ", last_name) as full_name, message, date_format(messages.created_at, "%M %D %Y") as created_date, messages.user_id, messages.id FROM users\
                    JOIN messages ON users.id = messages.user_id ORDER BY created_date DESC')
    comments = mysql.query_db('SELECT messages.user_id, comments.comment, comments.id, comments.message_id, date_format(comments.created_at, "%M %D %Y") as commented_date, messages.id, CONCAT(users.first_name, " ",users.last_name) AS full_name\
                                FROM messages LEFT JOIN comments ON messages.id = comments.message_id\
                                LEFT JOIN users ON comments.user_id = users.id ORDER BY commented_date ASC')

    return render_template('wall.html', user=user_id[0], messages=messages, comments=comments, user_id=user_id)

@app.route('/process', methods=['POST'])
def process():
    if 'id' not in session:
        return redirect('/')

    post = request.form['messages']
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) \
            VALUES(:user_id, :mess, NOW(), NOW())'
    data = {
            'user_id': session['id'],
            'mess': post
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    comment = request.form['comment']
    query = 'INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) \
    VALUES(:users_id, :mess_id, :user_comment, NOW(), NOW())'
    data = {
        'users_id': session['id'],
        'mess_id': message_id,
        'user_comment': comment
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<message_id>')
def delete(message_id):
    query1 = 'DELETE FROM messages WHERE id = :message'
    data1 = {
        'message': message_id
    }
    mysql.query_db(query1, data1)
    return redirect('/')
@app.route('/delete_comment/<comment_id>')
def delete_comment(comment_id):
    query = 'DELETE FROM comments WHERE message_id = :comment'
    data = {
        'comment': comment_id
    }
    mysql.query_db(query, data)
    return redirect('')
@app.route('/clear_session')                                               # Session clear
def clear():
    session.clear()
    return redirect('/')
app.run(debug=True)
