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


@phone_tracker_blueprint.route("/interactions-by-signal-strength", methods=['GET'])
def get_interactions_by_signal_strength():
    res = phone_tracker_service.get_interactions_by_signal_strength()
    return jsonify(res), 200


@phone_tracker_blueprint.route("/devices-by-dest-device/<device_id>", methods=['GET'])
def get_devices_by_dest_device(device_id):
    res = phone_tracker_service.get_devices_by_dest_device(device_id)
    return jsonify(res), 200


@phone_tracker_blueprint.route("/interaction-by-devices-ids/<device_a_id>/<device_b_id>", methods=['GET'])
def interaction_by_devices_ids(device_a_id: str, device_b_id: str):
    res = phone_tracker_service.interaction_by_devices_ids(device_a_id, device_b_id)
    return jsonify(res), 200
