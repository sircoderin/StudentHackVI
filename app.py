#!env/bin/python3

import json
import forms
import spotipy_utils
from flask import Flask, flash, redirect, render_template, request, session
from spotifyClient import *

app = Flask(__name__)
app.secret_key = 'ghghghtuy567iuyuyhnuybgt87frsw3'

global_results = []
home_tracks = []

spotify_playlist_id = credentials.spotify['playlist_id']
playlist_id = credentials.spotify['playlist_id']

@app.route('/')
def red_to_index():
	return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def home():

	global home_tracks

	if not session:
		if not session['name']:
			return redirect("/login")

	if request.method == 'POST':
		
		like = request.form.get('like')
		dislike = request.form.get('dislike')

		add_track = request.form.get('search')

		if add_track:
			return redirect('/search')

		if like:
			# todo call like method for the track_id (like)

			print("like")
			print(like)

		
		if dislike:
			# todo call the dislike method for the track_id (dislike)
			print("dislike")
			print(dislike)

		return redirect('/')

	home_tracks = read_playlist(playlist_id)

	return render_template("index.html", name=session['name'], tracks=home_tracks)


# Prompts user for a name
@app.route('/login', methods=['GET', 'POST'])
def login():
	
	if session['name']:
		return redirect('/index')

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
			spotipy_utils.add_to_playlist(track_id, spotify_playlist_id)

		return redirect('/index')

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

def getTracks():
	return home_tracks