from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import MySQLConnector
import re
import md5
app = Flask(__name__)
app.secret_key = 'iiuu#@#$%^&&*()'
mysql = MySQLConnector(app, 'login_registration')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation
NAME_REGEX = re.compile(r'^[^0-9]+$')                                      #string validation

@app.route('/')
def index():
    if "id" in session:                                                    #if id in session it will redirect to success.html
        return redirect('/success')
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
            query = 'INSERT INTO users(first_name, last_name, email, password, confirm_password, created_at, updated_at) VALUES(:f_name, :l_name, :user_email, :user_password, :password_confirm, NOW(), NOW())'
            data = {
                    'f_name':first_name,
                    'l_name': last_name,
                    'user_email':email,
                    'user_password':hashed_password,
                    'password_confirm':hashed_confirm_password
            }
            mysql.query_db(query, data)
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
            return redirect('/success')
        else:
            flash('Wrong password')
            return redirect('/')
    else:
        flash('email doesnt exist!')
        return redirect('/')
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/clear_session')                                               # Session clear
def clear():
    session.clear()
    return redirect('/')
app.run(debug=True)
