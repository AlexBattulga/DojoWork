from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    return "Got Post info"

    name = request.form['name']
    email = request.form['email']

    return redirect('/')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True)
