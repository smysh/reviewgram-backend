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
    response = requests.get(f"{search_url}movie",params=params,headers=headers)

    response.raise_for_status()
    
    movies_api = response.json()["results"]
    movies = []
    for movie in movies_api:
        new_movie = Movie.from_TMDB_to_Movie(movie)
        movies.append(new_movie.to_dict())

    # return movies

def get_TMDB_top_movies():
    url = f"{TMDB_URL}trending/movie/day"
    params = {
        "language":"en-US",
        "include_adult": False,
        "API_KEY":os.environ.get('TMDB_API_KEY')
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

def get_TMDB_movie_reviews(tmdb_id):
    url = f"{TMDB_URL}/movie/{tmdb_id}/reviews"
    params = {
        "language":"en-US"
    }

    response = requests.get(url,headers=headers,params=params)
    response.raise_for_status()

    tmdb_reviews = response.json()["results"]

    reviews = []
    for tmdb_review in tmdb_reviews:
        review = {
            "user": {
                "id": None,
                "username": tmdb_review["author"]
            },
            "content": tmdb_review["content"],
            "rating": tmdb_review["author_details"]["rating"],
            "created": tmdb_review["created_at"],
            "updated": tmdb_review["updated_at"],
            "fromTMDB": True
        }
        reviews.append(review)

    return reviews

#Later can be done by page
def get_TMDB_tv_show_reviews(tmdb_id):
    url = f"{TMDB_URL}/tv/{tmdb_id}/reviews"
    params = {
        "language":"en-US"
    }

    response = requests.get(url,headers=headers,params=params)
    response.raise_for_status()

    tmdb_reviews = response.json()["results"]

    reviews = []
    for tmdb_review in tmdb_reviews:
        review = {
            "user": {
                "id": None,
                "username": tmdb_review["author"]
            },
            "content": tmdb_review["content"],
            "rating": tmdb_review["author_details"]["rating"],
            "created": tmdb_review["created_at"],
            "updated": tmdb_review["updated_at"],
            "fromTMDB": True
        }
        reviews.append(review)

    return reviews

def get_images_url_from_TMDB():
    url = f"{TMDB_URL}/configuration"
    response = requests.get(url,headers=headers)
    response.raise_for_status()

    configuration = response.json()["images"]
    
    images_url_info = {}
    images_url_info["base_url"] = configuration["base_url"]
    images_url_info["secure_base_url"] = configuration["secure_base_url"]
    images_url_info["poster_sizes"] = configuration["poster_sizes"]
    return images_url_info



    