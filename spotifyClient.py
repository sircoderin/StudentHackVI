import spotipy
import sys
import spotipy.util as util
import credentials
import requests
import json
from ast import literal_eval
import login , spotipy_utils
from login import *
from track import *

def search_track(param):
	sp = spotipy.Spotify(spotipy_utils.get_token())
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

def play_track(id):
	id = "spotify:track:" + id
	sp = spotipy.Spotify(get_token())
	sp.start_playback(device_id = None, context_uri = None, uris = [id], offset = None)
	#print(sp.devices())

def remove_current(id):
	#user-read-playback-state
	sp = spotipy.Spotify(auth = "BQAbQdTvNbnH9CRcw2W2S34hoP9N5vUxj0CMm_sQHSBMK5H7HvCwUBv7-_H1B2LGT54CecWFJ9gtB3SitnHAStWYIUTKSE3ptJNEvKx7LldG--egOl3ZWjS8LhMwYzdGoAGpOlka3Vl5C42lOPMgYsSt5R_GHuMLYHTJHQsMsUpg6A")
	results = sp.current_playback()
	json_data = json.dumps(results, indent=2)

	#print(json_data)
	response = json_data.replace("'", '"')
	response = json_data.replace("\\", "")

	response = json.loads(response)
	output = []
	track_id = response['item']['id']

	#playlist-modify-public
	spotipy_utils.remove(track_id, id)


# Main method
if __name__ == "__main__":
	sp = spotipy.Spotify(get_token())
	#play_track("5cbpoIu3YjoOwbBDGUEp3P")
	remove_current("5OyaappkOODQPVWGZesvUr")

	#input = read_playlist("5OyaappkOODQPVWGZesvUr")
	#for each in input:
	#print(each.track_name)


	#output = search_track("martin garrix")
	#for item in output:
		#print ("%s by %s - %s" % (item.track_name, item.artist_name, item.track_id))
