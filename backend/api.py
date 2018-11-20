from flask import Flask

app = Flask(__name__)


@app.route("/")
def hell():
    print("API Functioning normally")
    return "Hello World!"