#!env/bin/python3

from flask import Flask
from flask import render_template
import credentials
import spotify_connect

app = Flask(__name__)

# spotify_connect = SpotifyConnect(credentials.spotify['user'], credentials.spotify['client_id'], credentials.spotify['client_secret'])

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

import json

@app.route('/login')
def login():
    return render_template('login.html')
