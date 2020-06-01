from flask import Flask, render_template, url_for, redirect, request, flash
from forms import Item, RegistrationForm, LoginForm
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from tkcalendar import DateEntry

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cba395a89aedb9322842accfb84d7817'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    identification = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    forms = Item()
    #if not forms.submit.validate(forms):
    #if request.method == 'POST' and forms.validate():
     #   item = request.form['food_item']
      #  exp_date = request.form['exp_date']
       # return render_template('view.html', item=item, exp_date=exp_date)
    return render_template('add.html', title='Add', forms=forms)

@app.route('/view', methods=['POST', 'GET'])
def view():
    return render_template('view.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = RegistrationForm()
    if request.method == 'POST' and forms.validate():
        flash('Registered Successfully', 'success')
        return redirect(url_for('add'))
    return render_template('register.html', forms=forms)

@app.route('/login', methods=['POST', 'GET'])
def login():
    forms = LoginForm()
    return render_template('login.html', forms=forms)

if __name__ == '__main__':
    app.run(debug=True)