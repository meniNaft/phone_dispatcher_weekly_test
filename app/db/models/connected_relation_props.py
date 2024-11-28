from datetime import datetime


class ConnectedRelationProps:
    from_device: str
    to_device: str
    method: str
    bluetooth_version: str
    signal_strength_dbm: int
    distance_meters: float
    duration_seconds: int
    timestamp: datetime
