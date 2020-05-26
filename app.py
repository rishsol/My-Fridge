from flask import Flask, render_template, url_for, redirect
from forms import Item

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cba395a89aedb9322842accfb84d7817'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    form  = [Item()]
    if form[len(form) - 1].validate_on_submit:
        form.append(Item())
        add()
    else:
        return render_template('add.html', title='Add', form=form)

if __name__ == '__main__':
    app.run(debug=True)