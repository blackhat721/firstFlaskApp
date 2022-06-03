from threading import main_thread
from flask import Flask
from pip import main

app = Flask(__name__)

@app.route('/')
def inital():
    return "hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)