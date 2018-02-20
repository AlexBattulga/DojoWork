from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)
app.secret_key = 'ihahdaohdoiahdoihaoihdo'

@app.route('/', methods=['get'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['fullname']
    location = request.form['location']
    language = request.form['lang']
    comment = request.form['comment']
    if len(name) < 1:
        flash("Name Cannot Be Empty!")
    else:
        flash('hey {}'.format(name))
    if len(comment) < 1:
        flash("Comment Cannot be empty!!!")
    elif len(comment) > 120:
        flash("No more than 120 characters!")
    else:
        flash("Success {}, you finally got it!".format(name))
    return render_template('result.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)
