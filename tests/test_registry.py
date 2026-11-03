from leafviewperiph.core.models import Capability, Device, Transport
from leafviewperiph.core.registry import DeviceRegistry


def test_registry_add_update_and_remove():
    registry = DeviceRegistry()
    device = Device("local:ble:1", "Test band", Transport.BLE,
                    capabilities=frozenset({Capability.DISCOVER, Capability.READ}))
    registry.add_or_update(device)
    assert registry.get(device.id) == device
    assert registry.get(device.id).supports(Capability.READ)
    updated = Device(device.id, "Renamed band", Transport.BLE)
    registry.add_or_update(updated)
    assert registry.get(device.id).name == "Renamed band"
    assert registry.remove(device.id)
    assert not registry.remove(device.id)


def test_registry_rejects_empty_identifier():
    registry = DeviceRegistry()
    try:
        registry.add_or_update(Device(" ", "Invalid", Transport.UNKNOWN))
    except ValueError:
        pass
    else:
        raise AssertionError("empty identifier should be rejected")
