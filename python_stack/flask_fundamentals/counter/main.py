from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mySecretKey'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/reload/plusTwo', methods=['post'])
def reload():
    session['counter'] += 2
    return redirect('/')

@app.route('/reload/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)
