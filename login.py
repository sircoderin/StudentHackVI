import sys
import spotipy
import spotipy.util as util


def get_token():
    token_file = "token.txt"
    f=open(token_file)
    token = f.read()
    return token

def get_user():
    sp = spotipy.Spotify(auth= get_token())
    sp.trace = False
    user = sp.current_user()
    user = user['uri'].split(':')
    return user[2]
