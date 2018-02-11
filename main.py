from flask import Flask, render_template, request
from models import db, Comments

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)

@app.route('/')
def root():
    comments = Comments.query.all()
    return render(comments=comments)

@app.route('/sign')
def sign():
    return render(template="sign")

# TEMPLATES
def render(template="home", comments=None):
    return render_template(template +".j2", comments=comments)


# API
@app.route('/process', methods=['POST'])
def proc():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)

    db.session.add(signature)
    db.session.commit()

    return root()


if __name__ == '__main__':
    """
    by default host=localhost and port=5000
    """
    app.run(debug=True, host="0.0.0.0")
