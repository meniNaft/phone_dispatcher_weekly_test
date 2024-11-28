from app.db.models.device import Device
from app.db.models.location import Location


def convert_json_to_device(json_dict: dict) -> Device:
    return Device(
        id=json_dict['id'],
        name=json_dict['name'],
        brand=json_dict['brand'],
        model=json_dict['model'],
        os=json_dict['os'],
        location=Location(**json_dict['location'])
    )


def get_api_message(message=None, data=None, error=None):
    res = {}
    if message:
        res['message'] = message
    if data:
        res['data'] = data
    if error:
        res['error'] = error

    return res