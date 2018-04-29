import sys
import spotipy
import spotipy.util as util


def get_token():
    token_file = "token.txt"
    f=open(token_file)
    token = f.read()
    return token

def get_playback_token(rw):
    token_file = "token.playback." + rw + ".txt"
    f=open(token_file)
    token = f.read()
    return token
