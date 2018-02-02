from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://ariel:ariel@localhost/flask-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET', 'POST'])
def root():
    return render()


@app.route('/home')
def home():
    return render("Home")


@app.route('/pages/<page>')
def pages(page):
    return render(page)


@app.route('/login')
def login():
    return render(template="login")


def render(var="World", template="template"):
    return render_template(template +".j2", var=var)


# API

@app.route('/process', methods=['POST'])
def proc():
    name = request.form['name']
    comment = request.form['comment']

    lan = name + " " + comment

    return render(var=lan)

if __name__ == '__main__':
    """
    by default host=localhost and port=5000
    """
    app.run(debug=True)
