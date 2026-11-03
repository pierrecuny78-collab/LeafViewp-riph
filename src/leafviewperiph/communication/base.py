"""Transport adapter protocol; implementations are platform-specific."""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from leafviewperiph.core.models import Device, Transport


@runtime_checkable
class TransportAdapter(Protocol):
    transport: Transport

    async def discover(self) -> list[Device]:
        """Return currently discoverable devices without modifying them."""
        ...

    async def close(self) -> None:
        """Release platform resources."""
        ...
