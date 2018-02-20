from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "thisisthesecretkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    email = request.form['email']
    fname = request.form['f_name']
    lname = request.form['l_name']
    password = request.form['password']
    confirm = request.form['confirm']
    if len(email) < 1:
        flash('Email cannot be empty!')
    elif not EMAIL_REGEX.match(email):
        flash('Invalid Email Address!')

    if len(fname) < 1:
        flash('First name cannot be empty!')
    elif not fname.isalpha():
        flash('First name cannot contain any numbers!')

    if len(lname) < 1:
        flash('Last name cannot be empty!')
    elif not lname.isalpha():
        flash('Last name cannot contain any numbers!')
    if len(password) < 1:
        flash('Password cannot be empty')
    elif len(password) < 8:
        flash('Password should be more than 8 characters!')
    elif not password == confirm:
        flash('Password is wrong!')
    else:
        flash('Thank you for submiting your information!')


    return redirect('/')
app.run(debug=True)
