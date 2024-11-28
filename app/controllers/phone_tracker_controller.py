from dataclasses import asdict
from flask import Blueprint, request, jsonify
import app.services.phone_tracker_service as phone_tracker_service
from app.db.models.device import Device

phone_tracker_blueprint = Blueprint("phone_tracker", __name__)


@phone_tracker_blueprint.route("/", methods=['POST'])
def get_interaction():
    data = request.json
    res = phone_tracker_service.handle_new_interaction(data)
    return jsonify(res), 200
