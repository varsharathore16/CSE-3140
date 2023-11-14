from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h>Team 12</h><p> Varsha & Maeve </p>"