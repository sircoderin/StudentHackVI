#!env/bin/python3

import credentials
import spotify_connect
import json

from flask import Flask, flash, redirect, render_template, request, session
from forms import *

app = Flask(__name__)
app.secret_key = 'ghghghtuy567iuyuyhnuybgt87frsw3'


@app.route('/')
def home():
    return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		name = NameForm(request.form)
		if name != "":
			session['name'] = name
			return redirect("/home")
		else:
			return render_template("login.html", error="Name cannot be empty!")

	return render_template('login.html')


@app.route('/search', methods=['GET', 'POST'])
def index():
	search = MusicSearchForm(request.form)
	if request.method == 'POST':
		return search_results(search)

	return render_template('search.html', form=search)


@app.route('/results')
def search_results(search):

	results = []
	search_string = search.data['search']

	# todo spotify search and save the results in the results var
	# results = spotifySearch(search_string)

	print(type(search))

	if not results:
		return render_template('results.html')
	else:
		# display results
		return render_template('results.html', results=results)
	
