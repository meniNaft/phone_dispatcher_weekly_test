from dataclasses import dataclass
from datetime import datetime
from app.db.models.device import Device


@dataclass
class DevicesInteraction:
    from_device: Device
    to_device: Device
    method: str
    bluetooth_version: str
    signal_strength_dbm: int
    distance_meters: float
    duration_seconds: int
    timestamp: datetime
