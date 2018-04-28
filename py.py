import spotipy
import sys
import spotipy.util as util
import requests

scope = 'user-library-read'
def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))

def add_to_playlist():
	scope = 'playlist-modify-public'
	username = sys.argv[1]
	playlist_id = '5OyaappkOODQPVWGZesvUr'
	track_ids = ['2Z8WuEywRWYTKe1NybPQEW']

	token = util.prompt_for_user_token(username, scope, client_id='4616f84bd6c344d49c4d49712de27d1d',client_secret='78fd807f7f06423b9d51f1e1fb4b8df3',redirect_uri='http://localhost:8181/')
	if token:
		sp = spotipy.Spotify(auth=token)
		sp.trace = False

		results =  sp.search("mockingbird", limit=10, offset=0, type='track', market=None)
		print(results)

		results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
		print(results)
	else:
		print("Can't get token for %s whatever" % username)

	#print sp.search("mockingbird", limit=10, offset=0, type='track', market=None)


# Main method
if __name__ == "__main__":
	add_to_playlist()
