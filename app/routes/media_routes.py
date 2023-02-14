from flask import Blueprint, request, jsonify, make_response, render_template
from app import db
from app.routes.TMDB_API_calls import get_TMDB_tv_show
from app.movie import Movie
from app.tvshow import TVShow
import urllib.request, json
import os

media_bp = Blueprint('media_bp', __name__, url_prefix="/media")



@media_bp.route("/search", methods=["GET"])
def search_media():
    url = f"https://api.themoviedb.org/3/search/multi?api_key={os.environ.get('TMDB_API_KEY')}&language=en-US&include_adult=false"
    search_for= request.args.get("query")
    url_append = f"&query={search_for}"
    url += url_append
    response = urllib.request.urlopen(url)
    data = response.read()
    return_data = json.loads(data)
    media_list = return_data["results"]
    media_dict = {}
    index = 0
    for media in media_list:
        if media["media_type"] == "movie":
            movie_obj = Movie.from_TMDB_to_Movie(media)
            media_dict[index] = movie_obj.to_dict()
            index += 1
        elif media["media_type"] == "tv":
            tvshow_obj = TVShow.from_TMDB_to_TVShow(media)
            media_dict[index] = tvshow_obj.to_dict()
            index += 1
    return media_dict

@media_bp.route("/top/movies", methods=["GET"])
def get_top_movies():
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={os.environ.get('TMDB_API_KEY')}&language=en-US&include_adult=false"
    response = urllib.request.urlopen(url)
    data = response.read()
    return_data = json.loads(data)
    movies_list = return_data["results"]
    movies_dict = {}
    index =0
    for movie in movies_list:
        movie_obj = Movie.from_TMDB_to_Movie(movie)
        movies_dict[index] = movie_obj.to_dict()
        index += 1
    return movies_dict

@media_bp.route("/top/tvshows", methods=["GET"])
def get_top_tvshows():
    url = f"https://api.themoviedb.org/3/trending/tv/day?api_key={os.environ.get('TMDB_API_KEY')}&language=en-US&include_adult=false"
    response = urllib.request.urlopen(url)
    data = response.read()
    return_data = json.loads(data)
    tvshows_list = return_data["results"]
    tvshows_dict = {}
    index =0
    for tvshow in tvshows_list:
        tvshow_obj = TVShow.from_TMDB_to_TVShow(tvshow)
        tvshows_dict[index] = tvshow_obj.to_dict()
        index += 1
    return tvshows_dict

@media_bp.route("/movies/<movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.environ.get('TMDB_API_KEY')}"
    response = urllib.request.urlopen(url)
    data = response.read()
    return_data = json.loads(data)
    movie_obj = Movie.from_TMDB_to_Movie(return_data)
   
    return movie_obj.to_dict()


@media_bp.route("/movies/<movie_id>/reviews", methods=["GET"])
def get_reviews_by_movie_id(movie_id):
    pass

@media_bp.route("/tv/<tmdb_tv_id>", methods=["GET"])
def get_tv_show_details_by_id(tmdb_tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tmdb_tv_id}?api_key={os.environ.get('TMDB_API_KEY')}"
    response = urllib.request.urlopen(url)
    data = response.read()
    return_data = json.loads(data)
    tv_obj = TVShow.from_TMDB_to_TVShow(return_data)
   
    return tv_obj.to_dict()
    # tv_show = get_TMDB_tv_show(tmdb_tv_id)

    # response_obj = {
    #     "statuscode": 200,
    #     "message": f"TV show with id: {tmdb_tv_id} retrieved from TMDB"
    # }

    #return response_obj


@media_bp.route("/tv/<tmdb_tv_id>/reviews", methods=["GET"])
def get_reviews_by_tv_id(tmdb_tv_id):
    pass
