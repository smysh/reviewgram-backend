from flask import Blueprint, request, jsonify, make_response, render_template, abort
from app import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.routes.helpers import validate_request_body

autho_bp = Blueprint('autho_bp', __name__, url_prefix="/token")

@autho_bp.route("", methods=["POST"])
def get_authorization_token():
    print("LLEGUE AL ROUTE")
    request_body = request.get_json(silent=True)
    validate_request_body(request_body,["username","password"])
    username = request_body["username"]
    password = request_body["password"]

    response_obj = {}

    if username != "test" or password != "test":
        response_obj["statuscode"] = 401
        response_obj["message"] = f"Invalid username or password"
        abort(make_response(jsonify(response_obj),500))

    access_token = create_access_token(identity=username)
    response_obj["statuscode"] = 201
    response_obj["message"] = f"Validated user: {username}"
    response_obj["token"] = access_token

    return jsonify(access_token)