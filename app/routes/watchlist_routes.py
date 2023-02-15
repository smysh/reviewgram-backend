from flask import Blueprint, request, jsonify, make_response
from app import db
from app.routes.user_routes import user_bp

@user_bp.route("/<user_id>/watchlist",methods = ["GET"])
def get_user_watchlist(user_id):
    pass

@user_bp.route("/<user_id>/watched",methods = ["GET"])
def get_user_watched(user_id):
    pass

@user_bp.route("/<user_id>/watchlist",methods = ["POST"])
def add_media_user_watchlist(user_id):
    pass

@user_bp.route("/<user_id>/watched",methods = ["POST"])
def add_media_user_watched(user_id):
    pass

@user_bp.route("/<user_id>/to-watched",methods = ["PATCH"])
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
