#!env/bin/python3

import credentials
import spotify_connect
import json

from flask import Flask
from flask import render_template
from flask import request, redirect, flash
from forms import MusicSearchForm
from spotifyClient import *

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("/login")

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
	search = MusicSearchForm(request.form)
	if request.method == 'POST':
		return search_results(search)

	return render_template('search.html', form=search)


def search_results(search):

	results = []
	search_string = search.data['search']

	if search_string == '':
		return redirect('/search')

	results = search_track(search_string)

	if not results:
		return render_template('results.html')
	else:
		#display results
		return render_template('results.html', results=results)
	
