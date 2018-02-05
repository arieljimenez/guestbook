from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ariel:ariel@localhost:3306/flask-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))


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

    signature = Comments(name=name, comment=comment)

    db.session.add(signature)
    db.session.commit()

    return render(var=name)

if __name__ == '__main__':
    """
    by default host=localhost and port=5000
    """
    app.run(debug=True, host="0.0.0.0")
