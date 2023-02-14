from flask import Blueprint, request, jsonify, make_response, abort
from app import db 
from app.routes.TMDB_API_calls import get_TMDB_tv_show, search_TMDB_media
from app.routes.helpers import validate_request_body

media_bp = Blueprint('media_bp', __name__, url_prefix="/media")

@media_bp.route("/search", methods=["GET"])
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
    response_obj["data"] = tv_show.to_json()

    return make_response(jsonify(response_obj),200)


@media_bp.route("/tv/<tmdb_tv_id>/reviews", methods=["GET"])
def get_reviews_by_tv_id(tmdb_tv_id):
    pass
