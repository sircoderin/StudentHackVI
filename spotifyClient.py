import spotipy
import sys
import spotipy.util as util
import credentials
import requests
import json
from ast import literal_eval
import spotipy_utils
from login import *

class Track(object):
	# track_name = ""
	# artist_name = ""
	# album_name = ""
	# track_id = ""
	# image_url = ""


	# The class "constructor" - It's actually an initializer
	def __init__(self, track_name, artist_name, album_name, track_id, image_url):
		self.track_name = track_name
		self.artist_name = artist_name
		self.album_name = album_name
		self.track_id = track_id
		self.image_url = image_url
		self.vote_count = 0

	def up_vote(self):
		self.vote_count+=1

	def down_vote(self):
		self.vote_count-=1

	def get_votes(self):
		return self.vote_count


def make_item(track_name, artist_name, album_name, track_id, image_url):
	item = Track(track_name, artist_name, album_name, track_id, image_url)
	return item


def search_track(param):
	sp = spotipy.Spotify(spotipy_utils.get_token())
	results =  sp.search(param, limit=10, offset=0, type='track', market=None)

	json_data = json.dumps(results, indent=2)

	response = json_data.replace("'", '"')
	response = json_data.replace("\\", "")

	response = json.loads(response)
	output = []
	for item in response['tracks']['items']:
		newObj = make_item(item['name'], item['album']['artists'][0]['name'], item['album']['name'], item['id'], item['album']['images'][2]['url'])
		output.append(newObj)
		#print("%s from album %s with id %s" % (item['name'], item['album']['name'], item['id']))
		#print(item['album']['images'][2]['url'])

	return output

def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		print("   %d %32.32s %s %s" % (i, track['artists'][0]['name'],
			track['name'], track['id']))

def read_playlist(id):
	username = get_user()
	sp = spotipy.Spotify(get_token())
	playlist = sp.user_playlist(username, playlist_id = id)
	
	if playlist['owner']['id'] == username:
		print(playlist['name'])
		print('  total tracks', playlist['tracks']['total'])
		results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
		tracks = results['tracks']
		show_tracks(tracks)
		while tracks['next']:
			tracks = sp.next(tracks)
			show_tracks(tracks)

def play_track(id):
    id = "spotify:track:" + id
    sp = spotipy.Spotify(get_token())
    sp.start_playback(device_id = None, context_uri = None, uris = [id], offset = None)

# Main method
if __name__ == "__main__":
	sp = spotipy.Spotify(spotipy_utils.get_token())
	sp.start_playback()


	#output = search_track("martin garrix")
	#for item in output:
		#print ("%s by %s - %s" % (item.track_name, item.artist_name, item.track_id))
	# read_playlist("5OyaappkOODQPVWGZesvUr")
