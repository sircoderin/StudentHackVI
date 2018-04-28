#!env/bin/python3

import json
import forms
from flask import Flask, flash, redirect, render_template, request, session
from spotifyClient import *

app = Flask(__name__)
app.secret_key = 'ghghghtuy567iuyuyhnuybgt87frsw3'


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


@app.route('/results')
def search_results(search_string):

	results = []

	if search_string == '':
		return redirect('/search')

	results = search_track(search_string)

	if not results:
		return render_template('results.html')
	else:
		# display results
		return render_template('results.html', results=results)
