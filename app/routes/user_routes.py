from flask import Blueprint, request, jsonify, make_response
from app import db
from app.routes.helpers import validate_request_body, validate_model
from app.models.user import User
from app.models.review import Review
from app.models.media import Media

user_bp = Blueprint('user_bp', __name__, url_prefix="/users")

@user_bp.route("/validate",methods = ["GET"])
def validate_user():
    pass

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

    review = Review.from_json(request_body)
    json_media = request_body["media"]
    media = Media.query.filter_by(is_movie=json_media["isMovie"],
                            TMDB_id=json_media["TMDB_id"]).first()
    if not media:
        media = Media.from_json(json_media)
        db.session.add(media)
        db.session.commit()

    review.media = media
    review.user = user

    db.session.add(review)
    db.session.commit()

    response_obj = {
        "statuscode": 201,
        "message": f"Successfully creting {user.user_name} review on {media.title}.",
        "review": review.to_json()
    }
    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>/reviews",methods = ["PATCH"])
def update_media_review(user_id):
    pass
