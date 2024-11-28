from flask import Blueprint, request, jsonify

phone_tracker_blueprint = Blueprint("phone_tracker", __name__)


@phone_tracker_blueprint.route("/", methods=['POST'])
def get_interaction():
    print(request.json)
    return jsonify({}), 200
