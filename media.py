import webbrowser

class Movie():
    """ This class provides a way to store movie related information including
    title, storyline, poster image, and online trailer video. """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ This is the constructor method which instantiates each movie with
        data provided in other functions """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function launches the trailer with the video contained
        in the trailer_youtube_url variable. """
        webbrowser.open(self.trailer_youtube_url)