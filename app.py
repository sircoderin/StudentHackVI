#!env/bin/python3

import credentials
import spotify_connect
import json
import spotipy_utils

from flask import Flask, flash, redirect, render_template, request, session
import forms
from spotifyClient import *

app = Flask(__name__)
app.secret_key = credentials.secret_key

global_results = []
spotify_playlist_id = '2NA4hjobhOjHhdHcDcpL7Z'

@app.route('/')
def home():
    return redirect("/login")


# Prompts user for a name
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		name = forms.NameForm(request.form)
		if name != "":
			session['name'] = name
			return redirect("/home")
		else:
			return render_template("login.html", error="Name cannot be empty!")

	return render_template('login.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
	search = forms.MusicSearchForm(request.form)
	if request.method == 'POST':
		return search_results(search)

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

def search_results(search):
	global global_results

	results = []
	search_string = search.data['search']

	if search_string == '':
		return redirect('/search')

	results = search_track(search_string)
	global_results = results

	if not results:
		return render_template('results.html')
	else:
		# display results
		return redirect('results')
	
