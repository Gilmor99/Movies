import webbrowser

class  Movie:
    """List the key attributes of the movies of the Best Film category of the
    Oscar 2017 nomenies."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube, director, release_date):
        """ Initialize the Movie object with the Title, storyline, link to the
        poter image, link to the YouTube trailer, Directort and Realease date.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.release_date = release_date

    def show_trailer(self):
        """ function calls the webbrowser.open function to
        play the YouTube trailer of the Movie's object.
        """
        webbrowser.open(self.youtube_trailer_url)
