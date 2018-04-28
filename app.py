#!env/bin/python3

import credentials
import spotify_connect
import json

from flask import Flask
from flask import render_template
from flask import request, redirect, flash
from forms import MusicSearchForm

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

@app.route('/results')
def search_results(search):

	results = []
	search_string = search.data['search']

<<<<<<< HEAD
	if search_string == '':
		return redirect('/search')

	# todo spotify search and save the results in the results var
	# results = spotifySearch(search_string)

	print(type(search))

	if not results:
		return render_template('results.html')
	else:
		#display results
		return render_template('results.html', results=results)
	
