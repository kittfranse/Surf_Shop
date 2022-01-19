#Import dependencies
from flask import Flask

# Flask App

app = Flask(__name__)

#Create a Flask routine
@app.route('/')
def hello_world():
    return 'Hello world'