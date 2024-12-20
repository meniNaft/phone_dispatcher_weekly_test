from app.db.database_config import driver
from app.db.models.device import Device
import app.utils.main_utils as device_utils


def get_device_by_uuid(uuid: str):
    with driver.session() as session:
        query = """
        match (d:Device {id: $uuid}) return d
        """

        params = {
            "uuid": uuid
        }

        res = session.run(query, params).single()
        return res.data()['d'] if res else None


def create_device(device: Device) -> Device:
    found_device = get_device_by_uuid(device.id)
    if found_device:
        return found_device
    else:
        with driver.session() as session:
            query = """
                create (d:Device {
                    id: $id,
                    brand: $brand,
                    name: $name,
                    model: $model,
                    os: $os,
                    latitude: $latitude,
                    longitude: $longitude,
                    altitude_meters: $altitude_meters,
                    accuracy_meters: $accuracy_meters
                })
                return d
                """

            params = {
                "id": device.id,
                "name": device.name,
                "brand": device.brand,
                "model": device.model,
                "os": device.os,
                "latitude": device.location.latitude,
                "longitude": device.location.longitude,
                "altitude_meters": device.location.altitude_meters,
                "accuracy_meters": device.location.accuracy_meters,
            }
            res = session.run(query, params).single()
            res = res.data()['d']
            return res if res else None
