from flask import Blueprint, request, jsonify, make_response
from app import db
from app.routes.helpers import validate_request_body
from app.models.user import User

user_bp = Blueprint('user_bp', __name__, url_prefix="/users")

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
        "user": new_user.to_dict()
    }
    
    return make_response(jsonify(response_obj), 201)

@user_bp.route("/<user_id>",methods = ["GET"])
def get_user_by_id(user_id):
    pass

@user_bp.route("/<user_id>",methods = ["PATCH"])
def update_user(user_id):
    pass

@user_bp.route("/<user_id>",methods = ["DELETE"])
def delete_user(user_id):
    pass

@user_bp.route("/<user_id>/reviews",methods = ["GET"])
def get_user_reviews(user_id):
    pass

@user_bp.route("/<user_id>/reviews",methods = ["POST"])
def add_media_review(user_id):
    pass

@user_bp.route("/<user_id>/reviews",methods = ["PATCH"])
def update_media_review(user_id):
    pass
