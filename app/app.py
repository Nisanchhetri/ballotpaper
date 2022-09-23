from flask import Flask

app = Flask(__name__)

@app.route('/')
def display():
    return "Welcome to starting page!!"
