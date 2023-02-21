from flask import Blueprint, request, jsonify, make_response, render_template, abort
from app import db
from app.models.media import Media
from app.routes.TMDB_API_calls import (get_TMDB_tv_show, 
                                        search_TMDB_media, 
                                        get_TMDB_top_movies, 
                                        get_TMDB_top_shows, 
                                        get_TMDB_movie,
                                        get_TMDB_tv_show_reviews,
                                        get_TMDB_movie_reviews,
                                        get_images_url_from_TMDB)
from app.routes.helpers import validate_request_body

media_bp = Blueprint('media_bp', __name__, url_prefix="/media")

@media_bp.route("/image-url", methods=["GET"])
def get_images_url():
    response_obj = {}
    try:
        images_url_config = get_images_url_from_TMDB()

    except Exception as err:
        print(f"An error occurred while getting url for images from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Images url configuration retrieved"
    response_obj["configuration"] = images_url_config

    return make_response(jsonify(response_obj),200)

@media_bp.route("/search", methods=["POST"])
def search_media():
    request_body = request.get_json(silent=True)
    validate_request_body(request_body, ["query"])
    query = request_body["query"]
    response_obj = {}
    
    try: 
        search_result = search_TMDB_media(query)

    except Exception as err:
        print(f"An error occured while searching from media with query: {query}")
        print(err)
        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Searching for: {query} successfull"
    response_obj["data"] = search_result

    return make_response(jsonify(response_obj),200)

@media_bp.route("/top/movies", methods=["GET"])
def get_top_movies():
    response_obj = {}
    try:
        top_movies = get_TMDB_top_movies()

    except Exception as err:
        print(f"An error occurred while getting top Movies from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Top movies retrieved from TMDB"
    response_obj["movies"] = top_movies

    return make_response(jsonify(response_obj),200)

@media_bp.route("/top/tvshows", methods=["GET"])
def get_top_tvshows():
    response_obj = {}
    try:
        top_tvshows = get_TMDB_top_shows()

    except Exception as err:
        print(f"An error occurred while getting top TV shows from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Top TV shows retrieved from TMDB"
    response_obj["tvshows"] = top_tvshows

    return make_response(jsonify(response_obj),200)

@media_bp.route("/movies/<tmdb_movie_id>", methods=["GET"])
def get_movie_by_id(tmdb_movie_id):
    response_obj = {}
    try:
        movie = get_TMDB_movie(tmdb_movie_id)

    except Exception as err:
        print(f"An error occurred while getting the movie with id: {tmdb_movie_id} from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Movie with id: {tmdb_movie_id} retrieved from TMDB"
    response_obj["movie"] = movie.to_dict()

    return make_response(jsonify(response_obj),200)

@media_bp.route("/tv/<tmdb_tv_id>", methods=["GET"])
def get_tv_show_details_by_id(tmdb_tv_id):
    response_obj = {}
    try:
        tv_show = get_TMDB_tv_show(tmdb_tv_id)

    except Exception as err:
        print(f"An error occurred while getting the tv_show with id: {tmdb_tv_id} from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        

    response_obj["statuscode"] = 200
    response_obj["message"]= f"TV show with id: {tmdb_tv_id} retrieved from TMDB"
    response_obj["tvshow"] = tv_show.to_json()

    return make_response(jsonify(response_obj),200)

#----------------Reviews for media endpoints ------------------

@media_bp.route("/tv/<tmdb_tv_id>/reviews", methods=["GET"])
def get_reviews_by_tv_id(tmdb_tv_id):
    response_obj = {}
    reviews = []
    try:
        tmdb_reviews = get_TMDB_tv_show_reviews(tmdb_tv_id)

    except Exception as err:
        print(f"An error occurred while getting reviews for TV show id: {tmdb_tv_id} from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        
    media = Media.query.filter_by(is_movie=False,
                            TMDB_id=tmdb_tv_id).first()
    if not media:
        reviews = tmdb_reviews
        media = Media(TMDB_id=tmdb_tv_id,is_movie=False)
    else:
        our_reviews = media.reviews
        if our_reviews:
            our_reviews.sort(reverse=True, key=lambda review: review.date_updated)
        reviews.extend(media.get_media_reviews_json())
        reviews.extend(tmdb_reviews)

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Reviews for tvshow with id: {tmdb_tv_id} retrieved Successfully"
    response_obj["reviews"] = reviews
    response_obj["media"] = media.get_media_info_json()

    return make_response(jsonify(response_obj),200)
    

@media_bp.route("/movies/<tmdb_movie_id>/reviews", methods=["GET"])
def get_reviews_by_movie_id(tmdb_movie_id):
    response_obj = {}
    reviews = []
    try:
        tmdb_reviews = get_TMDB_movie_reviews(tmdb_movie_id)

    except Exception as err:
        print(f"An error occurred while getting reviews for Movie id: {tmdb_movie_id} from TMDB API")
        print(err)

        response_obj["statuscode"] = 500
        response_obj["message"] = f"Problem accessing TMDB API"
        abort(make_response(jsonify(response_obj),500))
        
    media = Media.query.filter_by(is_movie=True,
                            TMDB_id=tmdb_movie_id).first()
    if not media:
        reviews = tmdb_reviews
        media = Media(TMDB_id=tmdb_movie_id,is_movie=True)
    else:
        our_reviews = media.reviews
        if our_reviews:
            our_reviews.sort(reverse=True, key=lambda review: review.date_updated)
        reviews.extend(media.get_media_reviews_json())
        reviews.extend(tmdb_reviews)

    response_obj["statuscode"] = 200
    response_obj["message"]= f"Reviews for Movie with id: {tmdb_movie_id} retrieved Successfully"
    response_obj["reviews"] = reviews
    response_obj["media"] = media.get_media_info_json()

    return make_response(jsonify(response_obj),200)
