class Movie():
    def __init__(self, TMDB_id, title, overview, poster_url, rating, vote_count, release_date="", original_language="", runtime=0, status="", genres=[], isMovie=True ):
        # movie_id
        self.TMDB_id = TMDB_id
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
        self.vote_count = vote_count
        # list of genres
        self.genres = genres
        # language code for movie language 'en' for english
        self.original_language = original_language
        # movie runtime 
        self.runtime = runtime
        # status of movie - Rumored, Planned, In Production, Post Production, Released, Canceled
        self.status = status
        # is it a movie or tv show
        self.isMovie = isMovie

    def get_search_result_dict(self):
        movie_dict = {
                "TMDB_id": self.TMDB_id,
                "title": self.title,
                "overview": self.overview,
                "poster_url": self.poster_url,
                "release_date": self.release_date,
                "rating": self.rating,
                "vote_count": self.vote_count,
                "original_language":self.original_language,
                "isMovie":self.isMovie,
        }
        return movie_dict

    def to_dict(self):
        """
        Returns dictionary of movie data.
        """
        movie_dict = {
                "TMDB_id": self.TMDB_id,
                "title": self.title,
                "overview": self.overview,
                "poster_url": self.poster_url,
                "release_date": self.release_date,
                "rating": self.rating,
                "vote_count": self.vote_count,
                "genres":self.genres,
                "original_language":self.original_language,
                "runtime":self.runtime,
                "status":self.status,
                "isMovie":self.isMovie,
        }
        return movie_dict
        
    @classmethod
    def from_TMDB_search_to_movie(cls, tmdb_movie_dict):
        return Movie(
            TMDB_id=tmdb_movie_dict["id"],
            title=tmdb_movie_dict["title"],
            overview=tmdb_movie_dict["overview"],
            poster_url=tmdb_movie_dict["poster_path"],
            original_language=tmdb_movie_dict["original_language"],
            release_date=tmdb_movie_dict["release_date"],
            rating=tmdb_movie_dict["vote_average"],
            vote_count=tmdb_movie_dict["vote_count"]
        )

    @classmethod
    def from_TMDB_to_Movie(cls, tmdb_movie_dict):
        """
        Creates movie instance from TMDB dict.
        """
        genres_list = []
        for genre in tmdb_movie_dict["genres"]:
            genres_list.append(genre["name"])

        tmdb_movie_dict.setdefault("runtime","unknown")
        tmdb_movie_dict.setdefault("status","unknown")
        tmdb_movie_dict.setdefault("isMovie",True)
        return Movie(
            TMDB_id=tmdb_movie_dict["id"],
            title=tmdb_movie_dict["title"],
            overview=tmdb_movie_dict["overview"],
            poster_url=tmdb_movie_dict["poster_path"],
            release_date=tmdb_movie_dict["release_date"],
            rating=tmdb_movie_dict["vote_average"],
            vote_count=tmdb_movie_dict["vote_count"],
            genres=genres_list,
            original_language=tmdb_movie_dict["original_language"],
            runtime=tmdb_movie_dict["runtime"],
            status=tmdb_movie_dict["status"],
            isMovie=tmdb_movie_dict["isMovie"]
        )



   
   
   
