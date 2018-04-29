import sys
import spotipy
import spotipy.util as util



from login import get_token

sp = spotipy.Spotify(auth= get_token())
sp.trace = False

def get_user():
	user = sp.current_user()
	user = user['uri'].split(':')
	return user[2]

#creates new playlit and returns id
def create_playlist(name):
	playlist = sp.user_playlist_create(get_user(), name, public=True)
	return playlist['id']

def get_playlist(id):
	return sp.user_playlist(get_user(), playlist_id=id, fields=None)

def add_to_playlist(track,playlist_id):
	sp.user_playlist_add_tracks(get_user(), playlist_id, [track])

#remove a track from playlist
def remove_from_playlist(track,playlist_id):
	sp.user_playlist_remove_all_occurrences_of_tracks(get_user(),playlist_id,[track],snapshot_id=None)

#return all IDs of the tracks from the playlist with given ID
def get_all_from_playlist(playlist_id):
	playlist = get_playlist(playlist_id)
	#get items
	items = playlist['tracks']['items']
	print items[1]['track']['id']
	id_list = []
	for item in items:
		id_list += [item['track']['id']]
	return id_list

def remove_all_from_playlist(playlist_id):
	track_id = get_all_from_playlist(playlist_id)
	for id in track_id :
		remove_from_playlist(id , playlist_id)


if __name__== '__main__':
	#mock_id = create_playlist('Dummy')
	#dummy tracks
	#track_uri = '5CMjjywI0eZMixPeqNd75R'
	mock_id = '1ouOPA7zXC3Rh0AAYOVErV'
	#add_to_playlist(track_uri,mock_id)
	#remove(track_uri,mock_id)
	remove_all_from_playlist(mock_id)




	#print get_user(get_token())
