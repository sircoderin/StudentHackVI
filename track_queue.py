from track import *
from spotipy_utils import *
from spotifyClient import *

class Track_Queue:
    queue = []

    #create a track queue from a spotify playlist with id playlist_id
    def __init__(self,playlist_id):
        self.playlist_id = playlist_id
        tracklist = get_playlist(playlist_id)['tracks']
        queue = []

        for i, item in enumerate(tracklist['items']):
            track = item['track']
            #print("   %d %32.32s %s %s" % (i, track['artists'][0]['name'],track['name'], track['id']))
            queue.append(Track(track['name'], track['artists'][0]['name'], track['album']['name'], track['id'], track['album']['images'][2]['url']))

        self.queue = queue
        self.sort()


    def get_playlist_id(self):
        return self.playlist_id

#queue sorting by vote_count funciton
    def sort(self):
        swap = True
        queue = self.queue
        #Bubble Sort
        while swap :
            swap = False
            for i in range(len(queue)-1):
                if queue[i].get_votes() < queue[i+1].get_votes() :
                    aux = queue[i]
                    queue[i] = queue[i+1]
                    queue[i+1] = aux
                    swap = True



    def export_to_spotify(self):
        queue = self.queue
        #clear playlist
        remove_all_from_playlist(self.playlist_id)
        #recreate the playlist
        for track in queue:
            add_to_playlist(track.getId(),self.playlist_id)



    def get_track_by_id(self, id):
        queue = self.queue
        for track in queue:
            if track.getId()==id:
                return track

    #add a track object
    def push(self, track, old_start):
        self.queue.append(track)
        self.sort()
        new_index = 0
        for i in range (len(queue))
            if queue[i].getId()==track_id:
                new_index = i
                break;
        reorder_track(old_start, new_index, self.playlist_id)
        #update spotify track
        #self.export_to_spotify()

    #delete all occurences of song with id track_id
    #returns the removed track object
    def pop(self,track_id):
        pop_track = None
        cuurent_ind = 0
        queue = self.queue
        for i in range (len(queue))
            if queue[i].getId()==track_id:
                pop_track = track
                self.queue.remove(track)   
                return (i, pop_track)
        return (0, None)
            # print track.getId()
        #update spotify track
        #self.export_to_spotify()

    def as_list(self):
        return self.queue
