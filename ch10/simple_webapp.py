from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1():
    return 'This is page 1.'


@app.route('/page2')
def page2():
    return 'This is page 2.'


@app.route('/page3')
def page3():
    return 'This is page 3.'


if __name__ == '__main__':
    app.run(debug=True)
