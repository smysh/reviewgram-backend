from flask import Blueprint, request, jsonify, make_response, render_template, abort
from app import db
from app.models.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.routes.helpers import validate_request_body

autho_bp = Blueprint('autho_bp', __name__, url_prefix="/token")

def validate_login(email,password):
    if email and password:
        user = User.query.filter_by(email=email,password=password).first()
    else:
        response_obj = {};
        response_obj["statuscode"] = 400
        response_obj["message"] = f"The email or password can't be empty"
        abort(make_response(jsonify(response_obj),400))

    return user

@autho_bp.route("", methods=["POST"])
def get_authorization_token():
    request_body = request.get_json(silent=True)
    validate_request_body(request_body,["email","password"])
    email = request_body["email"]
    password = request_body["password"]

    print(request_body)
    user = validate_login(email,password)

    response_obj = {}

    if not user:
        response_obj["statuscode"] = 401
        response_obj["message"] = f"Invalid email or password"
        abort(make_response(jsonify(response_obj),401))

    access_token = create_access_token(identity=email)
    response_obj["statuscode"] = 200
    response_obj["message"] = f"Validated user: {user.user_name}"
    response_obj["token"] = access_token
    response_obj["user"] = user.get_id_username_dict()

    return jsonify(response_obj)