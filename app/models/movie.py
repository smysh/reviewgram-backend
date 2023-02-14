class Movie():
    def __init__(self, id, title, overview, poster_url, release_date, rating, original_language, runtime, status, isMovie=True ):
        # movie_id
        self.id = id
        # movie's title
        self.title = title
        # brief description of movie
        self.overview = overview
        # path to movie .jpg file
        self.poster_url = poster_url
        # release date as a string
        self.release_date = release_date
        # vote_average from TMDB rating
        self.rating = rating
        # list of genres
        #self.genres = genres
        # language code for movie language 'en' for english
        self.original_language = original_language
        # movie runtime 
        self.runtime = runtime
        # status of movie - Rumored, Planned, In Production, Post Production, Released, Canceled
        self.status = status
        # is it a movie or tv show
        self.isMovie = isMovie

    def to_dict(self):
        """
        Returns dictionary of movie data.
        """
        movie_dict = {
                "id": self.id,
                "title": self.title,
                "overview": self.overview,
                "poster_url": self.poster_url,
                "release_date": self.release_date,
                "rating": self.rating,
                #"genres":self.genres,
                "original_language":self.original_language,
                "runtime":self.runtime,
                "status":self.status,
                "isMovie":self.isMovie,
        }
        return movie_dict
        
    @classmethod
    def from_TMDB_to_Movie(cls, tmdb_movie_dict):
        """
        Creates movie instance from TMDB dict.
        """
        #tmdb_movie_dict.setdefault("genres",[])
        tmdb_movie_dict.setdefault("runtime","unknown")
        tmdb_movie_dict.setdefault("status","unknown")
        tmdb_movie_dict.setdefault("isMovie",True)
        return Movie(
            id=tmdb_movie_dict["id"],
            title=tmdb_movie_dict["title"],
            overview=tmdb_movie_dict["overview"],
            poster_url=tmdb_movie_dict["poster_path"],
            release_date=tmdb_movie_dict["release_date"],
            rating=tmdb_movie_dict["vote_average"],
            #genres=tmdb_movie_dict["genres"],
            original_language=tmdb_movie_dict["original_language"],
            runtime=tmdb_movie_dict["runtime"],
            status=tmdb_movie_dict["status"],
            isMovie=tmdb_movie_dict["isMovie"]
        )



   
   
   
