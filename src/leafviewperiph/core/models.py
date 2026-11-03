"""Typed, transport-neutral device and capability models."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class Transport(StrEnum):
    BLUETOOTH_CLASSIC = "bluetooth-classic"
    BLE = "ble"
    WIFI = "wifi"
    WIFI_DIRECT = "wifi-direct"
    USB = "usb"
    USB_SERIAL = "usb-serial"
    UART = "uart"
    JTAG = "jtag"
    SWD = "swd"
    UNKNOWN = "unknown"


class Capability(StrEnum):
    DISCOVER = "discover"
    IDENTIFY = "identify"
    READ = "read"
    WRITE = "write"
    NOTIFY = "notify"
    INSTALL = "install"
    PROGRAM = "program"
    FIRMWARE_UPDATE = "firmware-update"
    RECOVERY = "recovery"
    DEBUG = "debug"


@dataclass(frozen=True, slots=True)
class Device:
    """A discovered peripheral; identifiers should be local and non-sensitive."""

    id: str
    name: str
    transport: Transport
    vendor: str | None = None
    model: str | None = None
    driver_id: str | None = None
    capabilities: frozenset[Capability] = field(default_factory=frozenset)
    metadata: dict[str, str] = field(default_factory=dict)

    def supports(self, capability: Capability) -> bool:
        return capability in self.capabilities
