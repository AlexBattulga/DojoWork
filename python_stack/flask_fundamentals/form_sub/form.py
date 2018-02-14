from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['fullname']
    location = request.form['location']
    language = request.form['lang']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)
