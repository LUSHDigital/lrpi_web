from flask import redirect, request, url_for, flash
import flask_app
from flask_app import app


@app.route('/', methods=['GET'])
def hello():
    print("hello")
    return "hello", 200


@app.route('/update-tracks', methods=['POST'])

def update_tracks():

    print("update_tracks")
    return "ok", 200
