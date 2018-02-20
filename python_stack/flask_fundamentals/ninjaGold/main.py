from flask import Flask, render_template, request, session, redirect
import random
import datetime
app = Flask(__name__)
app.secret_key = 'aabbccddfffgghhiii'

@app.route('/')
def index():
    if 'yourGolds' not in session:
        session['yourGolds'] = 0
        session['detailInfo'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['Post'])
def process_money():

    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %I:%M %p")

    if request.form['building'] == 'farm':
        goldEarned= random.randrange(10, 21)
        session['goldEarned'] = goldEarned
        message = 'Earned {} golds from the farm! ({})'.format(goldEarned, today)

        session['detailInfo'].insert(0, message)
    elif request.form['building'] == 'cave':
        goldEarned= random.randrange(5, 11)
        session['goldEarned'] = goldEarned
        message = 'Earned {} golds from the cave! ({})'.format(goldEarned, today)

        session['detailInfo'].insert(0, message)
    elif request.form['building'] == 'house':
        goldEarned= random.randrange(2, 6)
        session['goldEarned'] = goldEarned
        message = 'Earned {} golds from the house! ({})'.format(goldEarned, today)

        session['detailInfo'].insert(0, message)
    else:
        goldEarned= random.randrange(-50, 51)
        session['goldEarned'] = goldEarned
        if goldEarned >=0:
            message = 'Yay! You earned {} gold from the casino! ({})'.format(goldEarned, today)
        else:
            message = 'Entered a casino and lost {} golds...Ouch...({})'.format(goldEarned, today)

        session['detailInfo'].insert(0, message)
    session['yourGolds'] = session['yourGolds'] + goldEarned;

    return redirect('/')
@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)
