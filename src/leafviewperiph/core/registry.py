"""In-memory registry with stable-key replacement semantics."""
from __future__ import annotations

from leafviewperiph.core.models import Device


class DeviceRegistry:
    def __init__(self) -> None:
        self._devices: dict[str, Device] = {}

    def add_or_update(self, device: Device) -> None:
        if not device.id.strip():
            raise ValueError("device id must not be empty")
        self._devices[device.id] = device

    def remove(self, device_id: str) -> bool:
        return self._devices.pop(device_id, None) is not None

    def get(self, device_id: str) -> Device | None:
        return self._devices.get(device_id)

    def list(self) -> list[Device]:
        return sorted(self._devices.values(), key=lambda item: (item.name.casefold(), item.id))
