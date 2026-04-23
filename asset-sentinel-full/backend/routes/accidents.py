from flask import Blueprint, jsonify
accident_bp = Blueprint('accident', __name__)

@accident_bp.route("/accidents")
def get_accidents():
    return jsonify({"accidents": []})
