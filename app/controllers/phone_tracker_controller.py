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


@phone_tracker_blueprint.route("/bluetooth-and-path-long", methods=['GET'])
def get_bluetooth_and_path_long():
    res = phone_tracker_service.get_bluetooth_and_path_long()
    return jsonify(res), 200


def get_interactions_by_signal_strength():
    res = phone_tracker_service.get_interactions_by_signal_strength()
    return jsonify(res), 200
