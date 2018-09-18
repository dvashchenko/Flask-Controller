from flask import Flask #importing Flask class
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"
