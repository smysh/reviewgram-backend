from flask import Blueprint, request, jsonify, make_response
from app import db

media_bp = Blueprint('media_bp', __name__, url_prefix="media")

@media_bp.route("/search", methods=["POST"])
def search_media():
    pass

@media_bp.route("/top/movies", methods=["GET"])
def get_top_movies():
    pass

@media_bp.route("/top/tvshows", methods=["GET"])
def get_top_tvshows():
    pass

@media_bp.route("/movies/<movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    pass


@media_bp.route("/movies/<movie_id>/reviews", methods=["GET"])
def get_reviews_by_movie_id(movie_id):
    pass

@media_bp.route("/tv/<tv_id>", methods=["GET"])
def get_tvshows_by_id(tv_id):
    pass


@media_bp.route("/tv/<tv_id>/reviews", methods=["GET"])
def get_reviews_by_tv_id(tv_id):
    pass