from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'thisismysecretkey'
mysql = MySQLConnector(app, 'validate_email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def check():
    emails = request.form['email']
    pull_emails = 'SELECT * FROM emails WHERE email = :user_input'
    pull_data = {
                    'user_input': emails
    }
    check_emails = mysql.query_db(pull_emails, pull_data)
    session['user_email'] = emails

    if len(check_emails) == 0:
        if len(emails) < 1:
            flash('email cannot be empty!')
        elif not EMAIL_REGEX.match(emails):
            flash('Invalid Email Address!')
        else:
            query = 'INSERT INTO emails(email, created_at, updated_at) VALUE( :input_email, NOW(), NOW())'
            data = {
                    'input_email': emails
            }
            mysql.query_db(query, data)
            return redirect('/success')
    else:
        flash('email already exist!')
    return redirect('/')

@app.route('/success')
def success():
    query = 'SELECT email, DATE_FORMAT(created_at, "%m/%d/%y %r") as entered_date FROM emails'
    emails_in_db = mysql.query_db(query)
    flash('The email address you entered ({}) is a VALID email address! Thank you!'.format(session['user_email']))
    return render_template('success.html', all_emails = emails_in_db)
app.run(debug=True)
