from flask import Flask   #importing Flask class from a flask module
app = Flask(__name__) # class instance

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/HomePage')
def HomePage():
    return 'Hello, World!'


@app.route('/AboutUS')
def AboutUS():
    return 'Hello, World!'


@app.route('/ContactUs')
def ContactUs():
    return 'Hello, World!'