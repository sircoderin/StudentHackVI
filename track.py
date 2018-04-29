class Track(object):
    # track_name = ""
    # artist_name = ""
    # album_name = ""
    # track_id = ""
    # image_url = ""


    # The class "constructor" - It's actually an initializer
    def __init__(self, track_name, artist_name, album_name, track_id, image_url):
        self.track_name = track_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.track_id = track_id
        self.image_url = image_url
        self.vote_count = 0


    def getId(self):
        return self.track_id

    def up_vote(self):
        self.vote_count+=1

    def down_vote(self):
        self.vote_count-=1

    def get_votes(self):
        return self.vote_count

