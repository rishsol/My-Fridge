from flask import Flask, render_template, url_for, redirect, request, flash
from forms import Item, RegistrationForm, LoginForm
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from tkcalendar import DateEntry
import jinja2

app = Flask(__name__)
env = jinja2.Environment()
env.globals.update(zip=zip)
app.jinja_env.filters['zip'] = zip

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
    if request.method == 'POST':
        #soup = BeautifulSoup(open('templates/add.html'), 'html.parser')
        #print(list(soup.findAll('input', {'name': 'food'})))
        #items = [n.get('value') for n in soup.findAll('input', {'name': 'food'})]
        #print(items)
        #exp_dates = [n.get('value') for n in soup.findAll('input', {'name': 'date'})]
        items = request.form.getlist('food')
        print(items)
        exp_dates = request.form.getlist('date')
        return render_template('view.html', items=items, exp_dates=exp_dates) 
        #with open("templates/add.html", "r") as f:
         #   contents = f.read()
         #   soup = BeautifulSoup(contents, 'lxml')
         #   items = list(soup.findAll('td', attrs={'name': 'food'}))
          #  print(items)
           # exp_dates = list(soup.findAll('td', attrs={'name': 'item'}))
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