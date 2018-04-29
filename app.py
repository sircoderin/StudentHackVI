#!env/bin/python3

import json
import forms
import spotipy_utils
from flask import Flask, flash, redirect, render_template, request, session
from track_queue import *
from spotifyClient import *

app = Flask(__name__)
app.secret_key = 'ghghghtuy567iuyuyhnuybgt87frsw3'

global_results = []
home_tracks = []


spotify_playlist_id = credentials.spotify['playlist_id']
playlist_id = credentials.spotify['playlist_id']

song_queue = Track_Queue(playlist_id)
home_tracks = read_playlist(playlist_id)

# play_track(song_queue.get_most_wanted().getId(), song_queue)

@app.route('/')
def red_to_index():
	return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def home():

	global home_tracks
	global song_queue

	if not session:
		return redirect("/login")
		
	if request.method == 'POST':
		
		like = request.form.get('like')
		dislike = request.form.get('dislike')

		add_track = request.form.get('search')

		if add_track:
			return redirect('/search')

		if like:
			# todo call like method for the track_id (like)

			# for x in song_queue:
			# 	print(x.get_votes)

			(i,track) = song_queue.pop(like)
			track.up_vote()
			song_queue.push(track, i)


			print("like")
			print(like)
			# home_tracks = read_playlist(playlist_id)
			# song_queue.export_to_spotify()
		
		if dislike:
			# todo call the dislike method for the track_id (dislike)

			(i,track) = song_queue.pop(dislike)
			track.down_vote()
			song_queue.push(track, i)

			print("dislike")
			print(dislike)
			# home_tracks = read_playlist(playlist_id)
			# song_queue.export_to_spotify()

		return redirect('/')

	home_tracks = read_playlist(playlist_id)

	for track in song_queue.queue:
		print(track.track_name + "   " + str(track.get_votes()))

	return render_template("index.html", name=session['name'], tracks=home_tracks)


# Prompts user for a name
@app.route('/login', methods=['GET', 'POST'])
def login():
	
	if session and session['name']:
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
	global home_tracks
	global song_queue

	if request.method == 'POST':
		# print(request.form.get('add'))
		track_id = request.form.get('add')

		if track_id:
			spotipy_utils.add_to_playlist(track_id, spotify_playlist_id)
			home_tracks = read_playlist(playlist_id)
			i = 0
			for track in home_tracks:
				if track.track_id == track_id:
					song_queue.push(track, i)
					print(type(track))
					print('+++++++++++++++++++++++++++++++++++++++++++++')
				i=i+1

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