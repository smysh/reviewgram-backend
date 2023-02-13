from flask import Blueprint, request, jsonify, make_response
from app import db

tv_bp = Blueprint('tv_bp', __name__, url_prefix="/tv")

@tv_bp.route("<tmdb_tv_id>", methods = ["GET"])
def get_tv_show_details_by_id(tmdb_tv_id):

    response_obj = {
        "statuscode": 200,
        "message": f"TV show with id: {tmdb_tv_id} retrieved from TMDB"
    }

