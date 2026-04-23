from flask import Blueprint, jsonify
alert_bp = Blueprint('alerts', __name__)

@alert_bp.route("/alerts")
def alerts():
    return jsonify({"alerts": "No alerts"})
