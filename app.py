import json
from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercise3-02')
def exercise3_02():
	return render_template('exercise3a.html')

@app.route('/exercise3-03')
def exercise_03():
	return render_template('exercise3b.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

