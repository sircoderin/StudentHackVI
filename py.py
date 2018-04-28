import spotipy
import sys
import spotipy.util as util

username = '2cxjh5pqgk1ywrllnyl5sulk5'
scope = 'user-library-read'

util.prompt_for_user_token(username,scope,client_id='4616f84bd6c344d49c4d49712de27d1d',client_secret='78fd807f7f06423b9d51f1e1fb4b8df3',redirect_uri='http://localhost:8181/')

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username