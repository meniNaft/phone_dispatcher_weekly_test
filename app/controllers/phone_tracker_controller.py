from dataclasses import asdict
from sys import exception

from flask import Blueprint, request, jsonify
import app.services.phone_tracker_service as phone_tracker_service
from app.db.models.device import Device

phone_tracker_blueprint = Blueprint("phone_tracker", __name__)


@phone_tracker_blueprint.route("/", methods=['POST'])
def get_interaction():
    try:
        data = request.json
        res = phone_tracker_service.handle_new_interaction(data)
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400


@phone_tracker_blueprint.route("/bluetooth-and-path-long", methods=['GET'])
def get_bluetooth_and_path_long():
    try:
        res = phone_tracker_service.get_bluetooth_and_path_long()
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400


@phone_tracker_blueprint.route("/interactions-by-signal-strength", methods=['GET'])
def get_interactions_by_signal_strength():
    try:
        res = phone_tracker_service.get_interactions_by_signal_strength()
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400


@phone_tracker_blueprint.route("/devices-by-dest-device/<device_id>", methods=['GET'])
def get_devices_by_dest_device(device_id):
    try:
        res = phone_tracker_service.get_devices_by_dest_device(device_id)
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400


@phone_tracker_blueprint.route("/interaction-by-devices-ids/<device_a_id>/<device_b_id>", methods=['GET'])
def interaction_by_devices_ids(device_a_id: str, device_b_id: str):
    try:
        res = phone_tracker_service.interaction_by_devices_ids(device_a_id, device_b_id)
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400


@phone_tracker_blueprint.route("/last-interaction-by-caller-id/<caller_device_id>", methods=['GET'])
def get_last_interaction_by_caller_id(caller_device_id: str):
    try:
        res = phone_tracker_service.get_last_interaction_by_caller_id(caller_device_id)
        return jsonify(res), 200
    except exception() as e:
        return jsonify({str(e)}), 400
    