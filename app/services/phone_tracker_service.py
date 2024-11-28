from app.db.models.devices_interaction import DevicesInteraction
import app.db.repositories.device_repository as device_repo
import app.db.repositories.connected_relation_repository as connected_relation_repo
from app.utils.main_utils import convert_json_to_device


def handle_new_interaction(devices_interaction: dict):
    from_device = None
    to_device = None
    for elem in devices_interaction['devices']:
        if elem['id'] == devices_interaction['interaction']['from_device']:
            from_device = convert_json_to_device(elem)
        elif elem['id'] == devices_interaction['interaction']['to_device']:
            to_device = convert_json_to_device(elem)

    new_interaction = DevicesInteraction(
        from_device=from_device,
        to_device=to_device,
        method=devices_interaction['interaction']['method'],
        bluetooth_version=devices_interaction['interaction']['bluetooth_version'],
        signal_strength_dbm=devices_interaction['interaction']['signal_strength_dbm'],
        distance_meters=devices_interaction['interaction']['distance_meters'],
        duration_seconds=devices_interaction['interaction']['duration_seconds'],
        timestamp=devices_interaction['interaction']['timestamp'],
    )

    # 1. check device not call it self
    if new_interaction.from_device.id == new_interaction.to_device.id:
        return {"error": "a device cant call it self"}

    # 2. check device not call other device in same time (prevent duplicate)
    if connected_relation_repo.get_relation_by_devices_and_time(new_interaction):
        return {"error": "this interaction already exist"}

    device_a = device_repo.create_device(new_interaction.from_device)
    device_b = device_repo.create_device(new_interaction.to_device)
    res = connected_relation_repo.create_relation(new_interaction)
    return res


def get_bluetooth_and_path_long():
    return connected_relation_repo.get_bluetooth_and_path_long()


def get_interactions_by_signal_strength():
    return connected_relation_repo.get_interactions_by_signal_strength()


def get_devices_by_dest_device(device_id: str):
    return connected_relation_repo.get_devices_by_dest_device(device_id)
