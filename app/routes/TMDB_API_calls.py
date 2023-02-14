import requests
import os
from requests.structures import CaseInsensitiveDict
from app.models.tv_show import TVShow

MAX_RESULTS_PER_PAGE = 10
TMDB_URL = "https://api.themoviedb.org/3/"
TOKEN = os.environ.get("TMDB_BEARER_TOKEN")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {TOKEN}"

def get_TMDB_tv_show(tmdb_id):
    url = f"{TMDB_URL}tv/{tmdb_id}"
    response = requests.get(url,headers=headers)

    response.raise_for_status()

    tv_show= TVShow.from_dict(response.json())

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

def search_TMDB_media(query):
    search_url = f"{TMDB_URL}search/"
    params = {
        "query": query,
    }

    result = {
        "tv_shows": search_TMDB_tv_show(search_url,params),
        "movies": search_TMDB_movie(search_url, params)
    }

    print (result)

    return result


    