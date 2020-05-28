from flask import Flask, render_template, url_for, redirect, request
from forms import Item

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cba395a89aedb9322842accfb84d7817'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    forms = Item(request.form)
    while request.method == 'POST' and forms.validate():
        newForm = Item(request.form)
        return render_template('new_item.html', newForm=newForm)
    return render_template('add.html', title='Add', forms=forms)

@app.route('/view')
def view():
    return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True)