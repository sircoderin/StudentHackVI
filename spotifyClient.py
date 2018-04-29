import spotipy
import sys
import spotipy.util as util
import credentials
import requests
import json
from ast import literal_eval
import login
from login import *
from track import *
from spotipy_utils import *

def search_track(param):
	sp = spotipy.Spotify(get_token())
	results =  sp.search(param, limit=10, offset=0, type='track', market=None)

	json_data = json.dumps(results, indent=2)

	response = json_data.replace("'", '"')
	response = json_data.replace("\\", "")

	response = json.loads(response)
	output = []
	for item in response['tracks']['items']:
		newObj = Track(item['name'], item['album']['artists'][0]['name'], item['album']['name'], item['id'], item['album']['images'][2]['url'])
		output.append(newObj)
		#print("%s from album %s with id %s" % (item['name'], item['album']['name'], item['id']))
		#print(item['album']['images'][2]['url'])

	return output

def show_tracks(tracks):
		output = []
		for i, item in enumerate(tracks['items']):
				track = item['track']
				print("   %d %32.32s %s %s" % (i, track['artists'][0]['name'],track['name'], track['id']))
				newObj = Track(track['name'], track['artists'][0]['name'], track['album']['name'], track['id'], track['album']['images'][2]['url'])
				output.append(newObj)
		return output

def read_playlist(id):
	username = get_user()
	sp = spotipy.Spotify(get_token())
	playlist = sp.user_playlist(username, playlist_id = id)

	if playlist['owner']['id'] == username:
		print(playlist['name'])
		print('  total tracks', playlist['tracks']['total'])
		results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
		tracks = results['tracks']
		output = show_tracks(tracks)
		return output

def play_track(id, song_queue):
	full_id = "spotify:track:" + id
	sp = spotipy.Spotify(get_playback_token('write'))
	sp.start_playback(device_id = None, context_uri = None, uris = [full_id], offset = None)
	remove_current(song_queue.get_playlist_id())
	song_queue.pop(id)
	#print(sp.devices())

def remove_current(playlist_id):
	#user-read-playback-state
	sp = spotipy.Spotify(auth = get_playback_token('read') )
	results = sp.current_playback()
	json_data = json.dumps(results, indent=2)

	#print(json_data)
	response = json_data.replace("'", '"')
	response = json_data.replace("\\", "")

	response = json.loads(response)
	output = []
	track_id = response['item']['id']

	#playlist-modify-public
	remove_from_playlist(track_id, playlist_id)

def reorder_track(start, before, id):
	sp = spotipy.Spotify(get_token())
	sp.user_playlist_reorder_tracks(user = get_user(), playlist_id = id, range_start = start, insert_before = before, range_length = 1)

# Main method
if __name__ == "__main__":
	reorder_track(1, 0, "5OyaappkOODQPVWGZesvUr")
	#play_track("5cbpoIu3YjoOwbBDGUEp3P")
	#remove_current("5OyaappkOODQPVWGZesvUr")

	#input = read_playlist("5OyaappkOODQPVWGZesvUr")
	#for each in input:
	#print(each.track_name)


	#output = search_track("martin garrix")
	#for item in output:
		#print ("%s by %s - %s" % (item.track_name, item.artist_name, item.track_id))
