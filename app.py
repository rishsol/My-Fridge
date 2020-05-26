from flask import Flask, render_template, url_for
from flask_apscheduler import APScheduler

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)