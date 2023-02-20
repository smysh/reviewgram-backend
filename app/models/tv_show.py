class TVShow:
    def __init__(self, #The id of the media in our database
                    TMDB_id: int, 
                    name: str, 
                    overview: str,
                    rating: float, 
                    poster_url: str, 
                    vote_count: int,
                    original_language="",
                    origin_country="",
                    first_air_date="",
                    last_air_date="",
                    status="",
                    number_of_episodes=0,
                    number_of_seasons=0,
                    providers=[],
                    episode_runtime=[], 
                    genres=[]):

        self.TMDB_id = TMDB_id
        self.name = name
        self.overview = overview
        self.rating = rating
        self.poster_url = poster_url
        self.original_language = original_language
        self.origin_country = origin_country
        self.number_of_episodes = number_of_episodes
        self.number_of_seasons = number_of_seasons
        self.status = status
        self.first_air_date = first_air_date
        self.last_air_date= last_air_date
        self.providers = providers
        self.episode_runtime = episode_runtime
        self.genres = genres
        self.vote_count = vote_count

    def to_json(self):
        tv_show_dict = {}
        tv_show_dict["TMDB_id"] = self.TMDB_id
        tv_show_dict["name"] = self.name
        tv_show_dict["overview"] = self.overview
        tv_show_dict["rating"] = self.rating
        tv_show_dict["vote_count"] = self.vote_count
        tv_show_dict["poster_url"] = self.poster_url
        tv_show_dict["original_language"] = self.original_language
        tv_show_dict["origin_country"] = self.origin_country
        tv_show_dict["number_of_episodes"] = self.number_of_episodes
        tv_show_dict["number_of_seasons"] = self.number_of_seasons
        tv_show_dict["status"] = self.status
        tv_show_dict["first_air_date"] = self.first_air_date
        tv_show_dict["last_air_date"] = self.last_air_date
        tv_show_dict["providers"] = self.providers
        tv_show_dict["episode_runtime"] = self.episode_runtime
        tv_show_dict["genres"] = self.genres
        tv_show_dict["isMovie"] = False

        return tv_show_dict

    def get_search_result_dict(self):
        show = {}
        show["TMDB_id"] = self.TMDB_id
        show["name"] = self.name
        show["overview"] = self.overview
        show["origin_country"] = self.origin_country
        show["original_language"] = self.original_language
        show["first_air_date"] = self.first_air_date
        show["rating"] = self.rating
        show["poster_url"] = self.poster_url
        show["isMovie"] = False

        return show

    @classmethod
    def from_json(cls, tmdb_data):   #lacks providers
        genres_list = []
        for genre in tmdb_data["genres"]:
            genres_list.append(genre["name"])

        tv_show = TVShow(TMDB_id=tmdb_data["id"],
                    name=tmdb_data["name"],
                    overview=tmdb_data["overview"],
                    rating=tmdb_data["vote_average"],
                    poster_url=tmdb_data["poster_path"],
                    original_language=tmdb_data["original_language"],
                    origin_country=tmdb_data["origin_country"],
                    number_of_episodes=tmdb_data["number_of_episodes"],
                    number_of_seasons=tmdb_data["number_of_seasons"],
                    status=tmdb_data["status"],
                    first_air_date=tmdb_data["first_air_date"],
                    last_air_date=tmdb_data["last_air_date"],
                    episode_runtime=tmdb_data["episode_run_time"],
                    vote_count=tmdb_data["vote_count"],
                    genres=genres_list)

        return tv_show
        
    @classmethod
    def from_search(cls, tmdb_tv_search_result):
        tv_show = TVShow(TMDB_id=tmdb_tv_search_result["id"],
                    name=tmdb_tv_search_result["name"],
                    overview=tmdb_tv_search_result["overview"],
                    origin_country=tmdb_tv_search_result["origin_country"],
                    original_language=tmdb_tv_search_result["original_language"],
                    first_air_date=tmdb_tv_search_result["first_air_date"],
                    rating=tmdb_tv_search_result["vote_average"],
                    vote_count=tmdb_tv_search_result["vote_count"],
                    poster_url=tmdb_tv_search_result["poster_path"])

        return tv_show

