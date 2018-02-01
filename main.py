from flask import Flask, render_template

app = Flask(__name__)


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
    return ''

if __name__ == '__main__':
    """
    by default host=localhost and port=5000
    """
    app.run(debug=True)
