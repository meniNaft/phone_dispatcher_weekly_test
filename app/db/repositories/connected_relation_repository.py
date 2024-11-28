from app.db.database_config import driver
from app.db.models.devices_interaction import DevicesInteraction


def get_relation_by_devices_and_time(device_interaction: DevicesInteraction):
    with driver.session() as session:
        query = """
        match (d1:Device)-[c:CONNECTED {
        from_device: $from_device,
        to_device: $to_device,
        timestamp: $timestamp
        }]->(d2:Device)
        return c, d1, d2
        """

        params = {
            "from_device": device_interaction.from_device.id,
            "to_device": device_interaction.to_device.id,
            "timestamp": device_interaction.timestamp,
        }
        found_relation = session.run(query, params).single()
        return found_relation.data() if found_relation else None


def create_relation(devices_relation: DevicesInteraction):
    with driver.session() as session:
        query = """
        create (from_device: Device {id: $from_device})-[relation:CONNECTED {
            from_device: $from_device,
            to_device: $to_device,
            method: $method,
            bluetooth_version: $bluetooth_version,
            signal_strength_dbm: $signal_strength_dbm,
            distance_meters: $distance_meters,
            duration_seconds: $duration_seconds,
            timestamp: $timestamp
        }]->(to_device: Device {id: $to_device})
        return from_device, to_device, relation
        """

        params = {
            "from_device": devices_relation.from_device.id,
            "to_device": devices_relation.to_device.id,
            "method": devices_relation.method,
            "bluetooth_version": devices_relation.bluetooth_version,
            "signal_strength_dbm": devices_relation.signal_strength_dbm,
            "distance_meters": devices_relation.distance_meters,
            "duration_seconds": devices_relation.duration_seconds,
            "timestamp": devices_relation.timestamp,
        }
        res = session.run(query, params).data()
        return res if res else None