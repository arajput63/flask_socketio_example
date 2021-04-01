from flask import Flask, render_template, request
from flask_socketio import SocketIO

#import pandas as pd
#import numpy as np
#import random
#import datetime


app = Flask(__name__)
socketio = SocketIO(app=app, cors_allowed_origins='*')

@app.route("/", methods=['GET'])
def index():
    print("testingtest")
    return render_template("index.html")


@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/sockets")
def socket_page():
    return render_template("sockets.html")


@socketio.on('connect', namespace='/client')
def connect_sock():
    print("[ INFO ] SocketIO Client Connected: {}".format(request.sid))

@socketio.on('disconnect', namespace='/client')
def disconnect_sock():
    print("[ INFO ] SocketIO Client Disconnected: {}".format(request.sid))

@socketio.on('connect', namespace='/web')
def connect_web():
    print("[ INFO ] Web Client Connected: {}".format(request.sid))

@socketio.on('disconnect', namespace='/web')
def disconnect_web():
    print("[ INFO ] Web Client Disconnected: {}".format(request.sid))


@socketio.on('connect', namespace='/picam_stream')
def connect_cam():
    print('Picam Connected!')


if __name__ == "__main__":
    print("Test Message...")
    socketio.run(app=app, host="0.0.0.0", port="5000", debug=True)
    
