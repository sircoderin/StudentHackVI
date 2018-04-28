#!env/bin/python3

import json
import forms
import spotipy_utils
from flask import Flask, flash, redirect, render_template, request, session
from spotifyClient import *

app = Flask(__name__)
app.secret_key = 'ghghghtuy567iuyuyhnuybgt87frsw3'

global_results = []
spotify_playlist_id = '2NA4hjobhOjHhdHcDcpL7Z'

@app.route('/')
def home():
	if not session['name']:
		return redirect("/login")

	return render_template("index.html", name=session['name'])


# Prompts user for a name
@app.route('/login', methods=['GET', 'POST'])
def login():
	
	name_form = forms.NameForm(request.form)
	if request.method == "POST":
		if name_form.data['name'] != "":
			session['name'] = name_form.data['name']
			return redirect("/")
		else:
			return render_template("login.html", form=name_form, error="Name cannot be empty!")

	return render_template('login.html', form=name_form)


@app.route('/search', methods=['GET', 'POST'])
def search():
	if not session['name']:
		return redirect("/login")

	search = forms.MusicSearchForm(request.form)
	if request.method == 'POST':
		return search_results(search.data['search'])

	return render_template('search.html', form=search)


@app.route('/results',  methods=['GET', 'POST'])
def results():
	if request.method == 'POST':
		# print(request.form.get('add'))
		track_id = request.form.get('add')
		if track_id:
			add_to_playlist(track_id, spotify_playlist_id)

		return redirect('search')

	return render_template('results.html', results=global_results)

@app.route('/results')
def search_results(search_string):
	global global_results

	results = []

	if search_string == '':
		return redirect('/search')

	results = search_track(search_string)
	global_results = results

	if not results:
		return render_template('results.html')
	else:
		# display results
		return redirect('results')
