from flask import Flask
import socket

app = Flask(__name__)

@app.route('/name')
def name():
    name = socket.gethostname()
    return name

@app.route('/<x>/<y>')
def chaine(x,y):
    return x * y 

