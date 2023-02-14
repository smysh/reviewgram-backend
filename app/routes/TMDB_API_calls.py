import requests
import os
from requests.structures import CaseInsensitiveDict
from app.models.tv_show import TVShow
from app.models.movie import Movie

MAX_RESULTS_PER_PAGE = 10
TMDB_URL = "https://api.themoviedb.org/3/"
TOKEN = os.environ.get("TMDB_BEARER_TOKEN")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {TOKEN}"

def search_TMDB_media(query):
    url = f"{TMDB_URL}search/multi"
    params = {
        "language":"en-US",
        "include_adult": False,
        "API_KEY":os.environ.get('TMDB_API_KEY'),
        "query":query
    }
    response = requests.get(url,params=params,headers=headers)
    response.raise_for_status()
    
    media_list = response.json()["results"]
    media_dict = {}
    index = 0
    for media in media_list:
        if media["media_type"] == "movie":
            movie_obj = Movie.from_TMDB_to_Movie(media)
            media_dict[index] = movie_obj.to_dict()
            index += 1
        elif media["media_type"] == "tv":
            tvshow_obj = TVShow.from_search(media)
            media_dict[index] = tvshow_obj.get_search_result_dict()
            index += 1
    return media_dict
    
def get_TMDB_tv_show(tmdb_id):
    url = f"{TMDB_URL}tv/{tmdb_id}"
    response = requests.get(url,headers=headers)

    response.raise_for_status()

    tv_show= TVShow.from_json(response.json())

    return tv_show

def search_TMDB_tv_show(search_url,params):
    response = requests.get(f"{search_url}tv",params=params,headers=headers)

    response.raise_for_status()
    
    tvshows_api = response.json()["results"]
    tvshows = []
    for show in tvshows_api:
        new_show = TVShow.from_search(show)
        tvshows.append(new_show.get_search_result_dict())

    return tvshows

def get_TMDB_movie(tmdb_id):
    url = f"{TMDB_URL}movie/{tmdb_id}"
    response = requests.get(url,headers=headers)

    response.raise_for_status()

    movie_obj= Movie.from_TMDB_to_Movie(response.json())

    return movie_obj.to_dict()

def search_TMDB_movie(search_url, params):
    return search_TMDB_tv_show(search_url, params)
    # response = requests.get(f"{search_url}movie",params=params,headers=headers)

    # response.raise_for_status()
    
    # movies_api = response.json()["results"]
    # movies = []
    # for movie in movies_api:
    #     new_movie = TVShow.from_search(movie)
    #     movies.append(new_movie)

    # return movies

# def search_TMDB_media(query):
#     search_url = f"{TMDB_URL}search/"
#     params = {
#         "query": query,
#     }

#     result = {
#         "tv_shows": search_TMDB_tv_show(search_url,params),
#         "movies": search_TMDB_movie(search_url, params)
#     }

#     return result

def get_TMDB_top_movies():
    url = f"{TMDB_URL}trending/movie/day"
    params = {
        "language":"en-US",
        "include_adult": False,
        "API_KEY":'edb70fb19e9dd1cc6a0954ab333d8a04'
    }
    response = requests.get(url,params=params,headers=headers)

    response.raise_for_status()
    movies_list = response.json()["results"]
    movies_dict = {}
    index =0
    for movie in movies_list:
        movie_obj = Movie.from_TMDB_to_Movie(movie)
        movies_dict[index] = movie_obj.to_dict()
        index += 1
    return movies_dict

def get_TMDB_top_shows():
    url = f"{TMDB_URL}trending/tv/day"
    params = {
        "language":"en-US",
        "include_adult": False,
        "API_KEY":'edb70fb19e9dd1cc6a0954ab333d8a04'
    }
    response = requests.get(url,params=params,headers=headers)

    response.raise_for_status()
    tvshows_list = response.json()["results"]
    tvshows_dict = {}
    index =0
    for tvshow in tvshows_list:
        tvshow_obj = TVShow.from_search(tvshow)
        tvshows_dict[index] = tvshow_obj.get_search_result_dict()
        index += 1
    return tvshows_dict



    