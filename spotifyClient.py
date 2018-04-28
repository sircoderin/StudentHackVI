import spotipy
import sys
import spotipy.util as util
import credentials
import requests
import json
from ast import literal_eval
from spotipy_utils import *

class Item(object):
    track_name = ""
    album_name = ""
    track_id = ""
    image_url = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, track_name, album_name, track_id, image_url):
        self.track_name = track_name
        self.album_name = album_name
        self.track_id = track_id
        self.image_url = image_url

def make_item(track_name, album_name, track_id, image_url):
    item = Item(track_name, album_name, track_id, image_url)
    return item


def search_track(param):
    sp = spotipy.Spotify(get_token())
    results =  sp.search(param, limit=10, offset=0, type='track', market=None)

    json_data = json.dumps(results, indent=2)

    response = json_data.replace("'", '"')
    response = json.loads(response)
    output = []
    for item in response['tracks']['items']:
        newObj = make_item(item['name'], item['album']['name'], item['id'], item['album']['images'][2]['url'])
        output.append(newObj)
        #print("%s from album %s with id %s" % (item['name'], item['album']['name'], item['id']))
        #print(item['album']['images'][2]['url'])

    return output


# Main method
if __name__ == "__main__":
    # add_to_playlist()
    output = search_track("Lose Yourself")
    for item in output:
        print ("%s - %s" % (item.track_name, item.track_id))
