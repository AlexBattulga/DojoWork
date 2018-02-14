from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', ninjas = ['Black ninja - Smart', 'Yellow ninja - Fast', 'Red ninja - Brave', 'Blue ninja - Freindly'])

@app.route('/dojos/new')
def form():
    return render_template('dojos.html')
app.run(debug=True)
