class TVShow():
    def __init__(self, id, title, overview, poster_url, number_of_seasons, number_of_episodes, rating, first_air_date, last_air_date, original_language, episode_run_time, status, media_type="tv" ):
        # tvshow_id
        self.id = id
        # tv show's title
        self.title = title
        # brief description of tvshow
        self.overview = overview
        # path to tvshow .jpg file
        self.poster_url = poster_url
        # number of seasons
        self.number_of_seasons = number_of_seasons
        # number of episodes
        self.number_of_episodes = number_of_episodes
        # vote_average from TMDB rating
        self.rating = rating
        # first air date as a string
        self.first_air_date = first_air_date
        # last air date as a string
        self.last_air_date = last_air_date
        # list of genres
        #self.genres = genres
        # language code for movie language 'en' for english
        self.original_language = original_language
        # tv show episode runtime 
        self.episode_run_time = episode_run_time
        # status of tvshow - 
        self.status = status
        # is it a movie or tv show
        self.media_type = media_type

    def to_dict(self):
        """
        Returns dictionary of movie data.
        """
        tv_dict = {
                "id": self.id,
                "title": self.title,
                "overview": self.overview,
                "poster_url": self.poster_url,
                "number_of_seasons": self.number_of_seasons,
                "number_of_episodes": self.number_of_episodes,
                "first_air_date": self.first_air_date,
                "last_air_date": self.last_air_date,
                "rating": self.rating,
                #"genres":self.genres,
                "original_language":self.original_language,
                "runtime":self.episode_run_time,
                "status":self.status,
                "media_type":self.media_type
        }
        return tv_dict
        
    @classmethod
    def from_TMDB_to_TVShow(cls, tmdb_tvshow_dict):
        """
        Creates TVShow instance from TMDB dict.
        """
        tmdb_tvshow_dict.setdefault("number_of_seasons", "unknown") 
        tmdb_tvshow_dict.setdefault("number_of_episodes", "unknown")
        #tmdb_tvshow_dict.setdefault("genres",[])
        tmdb_tvshow_dict.setdefault("last_air_date", "unknown")
        tmdb_tvshow_dict.setdefault("episode_run_time","unknown")
        tmdb_tvshow_dict.setdefault("status","unknown")
        tmdb_tvshow_dict.setdefault("media_type","movie")
        return TVShow(
            id=tmdb_tvshow_dict["id"],
            title=tmdb_tvshow_dict["name"],
            overview=tmdb_tvshow_dict["overview"],
            poster_url=tmdb_tvshow_dict["poster_path"],
            number_of_seasons=tmdb_tvshow_dict["number_of_seasons"], 
            number_of_episodes=tmdb_tvshow_dict["number_of_episodes"],
            first_air_date=tmdb_tvshow_dict["first_air_date"],
            last_air_date=tmdb_tvshow_dict["last_air_date"],
            rating=tmdb_tvshow_dict["vote_average"],
            #genres=tmdb_tvshow_dict["genres"],
            original_language=tmdb_tvshow_dict["original_language"],
            episode_run_time=tmdb_tvshow_dict["episode_run_time"],
            status=tmdb_tvshow_dict["status"],
            media_type=tmdb_tvshow_dict["media_type"]
        )

