from flask import Flask

from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_html(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
