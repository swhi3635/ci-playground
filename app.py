# flask_web/app.py

from flask import Flask, request, escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have a Flask app!'

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
