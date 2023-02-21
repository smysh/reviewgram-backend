import time
from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.routes.helpers import validate_request_body, validate_model
from app.models.user import User
from app.models.review import Review
from app.models.media import Media
from app.models.watchlist import Watchlist
from datetime import datetime
from app.routes.TMDB_API_calls import get_TMDB_movie, get_TMDB_tv_show


user_bp = Blueprint('user_bp', __name__, url_prefix="/users")


#------------------CRUD routes for user--------------------
@user_bp.route("",methods = ["POST"])
def create_user():
    request_body = request.get_json(silent=True) #Silent=True prevents Exceptions from being raised
    validate_request_body(request_body,["name","email","username","password"])

    new_user = User.from_json(request_body)
    
    db.session.add(new_user)
    db.session.commit()
    
    response_obj = {
        "statuscode": 201,
        "message": f"User: {new_user.user_name} created successfully.",
        "user": new_user.get_user_data_json()
    }

    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>",methods = ["GET"])
def get_user_by_id(user_id):
    user = validate_model(User,user_id)

    response_obj = {
        "statuscode": 200,
        "message": f"Successfully retrieved {user.user_name}.",
        "user": user.get_user_data_json()
    }

    return make_response(jsonify(response_obj), 200)

@user_bp.route("/<user_id>",methods = ["PATCH"])
def update_user(user_id):
    pass

@user_bp.route("/<user_id>",methods = ["DELETE"])
def delete_user(user_id):
    pass

#--------------------Review routes-------------------

@user_bp.route("/<user_id>/reviews",methods = ["GET"])
def get_user_reviews(user_id):
    user = validate_model(User,user_id)

    reviews = []
    for review in user.reviews:
        reviews.append(review.to_json())

    response_obj = {
        "statuscode": 200,
        "message": f"Successfully retrieved {user.user_name} reviews.",
        "reviews": reviews
    }
    return make_response(jsonify(response_obj), 200)

@user_bp.route("/<user_id>/reviews",methods = ["POST"])
def add_media_review(user_id):
    user = validate_model(User, user_id)
    request_body = request.get_json(silent=True)
    validate_request_body(request_body, ["content","rating","media"])
    validate_request_body(request_body["media"],["TMDB_id","isMovie","title"])

    json_media = request_body["media"]
    media = Media.query.filter_by(is_movie=json_media["isMovie"],
                            TMDB_id=json_media["TMDB_id"]).first()
    if not media:
        media = Media.from_json(json_media)
        db.session.add(media)
        db.session.commit()

    review = Review.query.filter_by(user=user,media=media).first()

    if not review:
        review = Review.from_json(request_body)
        review.media = media
        review.user = user
        review.date_created = datetime.now()
        review.date_updated = review.date_created
        db.session.add(review)
        db.session.commit()
    else:
        review.content = request_body["content"]
        review.rating = request_body["rating"]
        review.updated = datetime.now()
        db.session.commit()

        

    response_obj = {
        "statuscode": 201,
        "message": f"Successfully creating {user.user_name} review on {media.title}.",
        "review": review.to_json()
    }
    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>/reviews",methods = ["PATCH"])
def update_media_review(user_id):
    pass

#------------------Watchlist routes------------------------
@user_bp.route("/<user_id>/watchlist",methods = ["GET"])
def get_user_watchlist(user_id):
    user = validate_model(User,user_id)

    watchlist_query = Watchlist.query.filter(Watchlist.user_id==user_id, 
                                            Watchlist.watched==False).all()
    watchlist = []
    for entry in watchlist_query:
        try:
            if entry.media.is_movie:
                json_entry = entry.to_json()
                movie = get_TMDB_movie(entry.media.TMDB_id)
                json_entry["media"] = movie.get_search_result_dict()
                watchlist.append(json_entry)
                time.sleep(0.25)
            else:
                json_entry = entry.to_json()
                json_entry["media"] = get_TMDB_tv_show(entry.media.TMDB_id).get_search_result_dict()
                watchlist.append(json_entry)
                time.sleep(0.25)

        except Exception as err:
            print(f"An error occurred getting watchlist data from TMDB API")
            print(err)

            response_obj["statuscode"] = 500
            response_obj["message"] = f"Problem accessing TMDB API"
            abort(make_response(jsonify(response_obj),500))

    response_obj = {
        "statuscode": 200,
        "message": f"Successfully getting {user.user_name} watchlist.",
        "watchlist": watchlist
    }
    return make_response(jsonify(response_obj), 200)

@user_bp.route("/<user_id>/watched",methods = ["GET"])
def get_user_watched(user_id):
    user = validate_model(User,user_id)

    watchlist_query = Watchlist.query.filter(Watchlist.user_id==user_id, 
                                            Watchlist.watched==True).all()

    watched = []
    for entry in watchlist_query:
        try:
            if entry.media.is_movie:
                json_entry = entry.to_json()
                json_entry["media"] = get_TMDB_movie(entry.media.TMDB_id).get_search_result_dict()
                watched.append(json_entry)
                time.sleep(0.25)
            else:
                json_entry = entry.to_json()
                json_entry["media"] = get_TMDB_tv_show(entry.media.TMDB_id).get_search_result_dict()
                watched.append(json_entry)
                time.sleep(0.25)

        except Exception as err:
            print(f"An error occurred getting watched list data from TMDB API")
            print(err)

            response_obj["statuscode"] = 500
            response_obj["message"] = f"Problem accessing TMDB API"
            abort(make_response(jsonify(response_obj),500))

    response_obj = {
        "statuscode": 200,
        "message": f"Successfully getting {user.user_name} watched list.",
        "watched": watched
    }
    return make_response(jsonify(response_obj), 200)

@user_bp.route("/<user_id>/watchlist",methods = ["POST"])
def add_media_user_watchlist(user_id):
    user = validate_model(User,user_id)
    request_body = request.get_json(silent=True)
    validate_request_body(request_body, ["TMDB_id","isMovie","title"])

    media = Media.query.filter_by(is_movie=request_body["isMovie"],
                            TMDB_id=request_body["TMDB_id"]).first()
    if not media:
        media = Media.from_json(request_body)
        db.session.add(media)
        db.session.commit()

    entry = Watchlist.query.filter_by(user=user,media=media).first()

    if not entry:
        entry = Watchlist(watched=False)
        entry.user = user
        entry.media = media
        db.session.add(entry)
        db.session.commit()

    elif entry.watched:
        entry.watched = False
        db.session.commit()

    response_obj = {
        "statuscode": 201,
        "message": f"Successfully adding {media.title} to {user.user_name} watchlist",
        "entry": entry.to_json()
    }
    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>/watched",methods = ["POST"])
def add_media_user_watched(user_id):
    user = validate_model(User,user_id)
    request_body = request.get_json(silent=True)
    validate_request_body(request_body, ["TMDB_id","isMovie","title"])

    media = Media.query.filter_by(is_movie=request_body["isMovie"],
                            TMDB_id=request_body["TMDB_id"]).first()
    if not media:
        media = Media.from_json(request_body)
        db.session.add(media)
        db.session.commit()

    entry = Watchlist.query.filter_by(user=user,media=media).first()

    if not entry:
        entry = Watchlist(watched=True)
        entry.user = user
        entry.media = media
        db.session.add(entry)
        db.session.commit()

    elif not entry.watched:
        entry.watched = True
        db.session.commit()

    response_obj = {
        "statuscode": 201,
        "message": f"Successfully adding {media.title} to {user.user_name} watched list",
        "entry": entry.to_json()
    }
    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>/watchlist/<watchlist_id>",methods = ["PATCH"])
def add_media_from_user_watchlist_to_watched(user_id):
    pass

@user_bp.route("/<user_id>/to-watchlist",methods = ["PATCH"])
def add_media_from_user_watched_to_watchlist(user_id):
    pass

@user_bp.route("/<user_id>/watched",methods = ["DELETE"])
def delete_media_from_user_watched(user_id):
    pass

@user_bp.route("/<user_id>/watchlist",methods = ["DELETE"])
def delete_media_from_user_watchlist(user_id):
    pass
