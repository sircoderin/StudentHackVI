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
def remove(track,playlist_id):
    sp.user_playlist_remove_all_occurrences_of_tracks(get_user(),playlist_id,[track],snapshot_id=None)

if __name__== '__main__':
    #mock_id = create_playlist('Dummy')
    #dummy tracks
    track_uri = '5CMjjywI0eZMixPeqNd75R'
    mock_id = '2NA4hjobhOjHhdHcDcpL7Z'
    add_to_playlist(track_uri,mock_id)
    #remove(track_uri,mock_id)


    #print get_user(get_token())
