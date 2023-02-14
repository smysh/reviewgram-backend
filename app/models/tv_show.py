class TVShow:
    def __init__(self, #The id of the media in our database
                    TMDB_id: int, 
                    name: str, 
                    overview: str,
                    rating: float, 
                    poster_url: str, 
                    original_language: str,
                    number_of_episodes: int,
                    number_of_seasons: int,
                    status: str,
                    first_air_date: str,
                    last_air_date: str,
                    id=-1,
                    providers=[],
                    episode_runtime=[], 
                    genres=[]):

        self.id = id
        self.TMDB_id = TMDB_id
        self.name = name
        self.overview = overview
        self.rating = rating
        self.poster_url = poster_url
        self.original_language = original_language
        self.number_of_episodes = number_of_episodes
        self.number_of_seasons = number_of_seasons
        self.status = status
        self.first_air_date = first_air_date
        self.last_air_date= last_air_date
        self.providers = providers
        self.episode_runtime = episode_runtime
        self.genres = genres

    def to_dict(self):
        tv_show_dict = {}
        tv_show_dict["id"] = self.id
        tv_show_dict["TMDBid"] = self.TMDB_id
        tv_show_dict["name"] = self.name
        tv_show_dict["overview"] = self.overview
        tv_show_dict["rating"] = self.rating
        tv_show_dict["original_language"] = self.original_language
        tv_show_dict["number_of_episodes"] = self.number_of_episodes
        tv_show_dict["number_of_seasons"] = self.number_of_seasons
        tv_show_dict["status"] = self.status
        tv_show_dict["first_air_date"] = self.first_air_date
        tv_show_dict["last_air_date"] = self.last_air_date
        tv_show_dict["providers"] = self.providers
        tv_show_dict["episode_runtime"] = self.episode_runtime
        tv_show_dict["genres"] = self.genres

        return tv_show_dict

    @classmethod
    def from_dict(cls, tmdb_data):
        genres_list = []
        for genre in tmdb_data["genres"]:
            genres_list.append(genre["name"])

        tv_show = TVShow(TMDB_id=tmdb_data["id"],
                    name=tmdb_data["name"],
                    overview=tmdb_data["overview"],
                    rating=tmdb_data["vote_average"],
                    poster_url=tmdb_data["backdrop_path"],
                    original_language=tmdb_data["original_language"],
                    number_of_episodes=tmdb_data["number_of_episodes"],
                    number_of_seasons=tmdb_data["number_of_seasons"],
                    status=tmdb_data["status"],
                    first_air_date=tmdb_data["first_air_date"],
                    last_air_date=tmdb_data["last_air_date"],
                    episode_runtime=tmdb_data["episode_run_time"],
                    genres=genres_list)

        return tv_show
        


