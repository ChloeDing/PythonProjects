import webbrowser

class Movie():
    ''' some documents '''
    VALID_RATINGS = ["R", "PG-13", "PG", "G", "NC-17"]
    
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
