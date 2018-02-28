from flask import Flask, request, render_template, redirect
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')
@app.route('/')
def index():
    query = 'SELECT full_name, age, DATE_FORMAT(started_date, "%M %D") as friend_since, YEAR(started_date) as year FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    age = request.form['age']
    query = 'INSERT INTO friends(full_name, age, started_date) VALUES(:name, :age, NOW())'
    data = {
            'name': name,
            'age': age
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
