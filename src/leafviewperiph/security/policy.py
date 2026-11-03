"""Fail-closed policy for operations that can modify a device."""
from __future__ import annotations

from enum import StrEnum


class Operation(StrEnum):
    DISCOVER = "discover"
    DIAGNOSE = "diagnose"
    READ = "read"
    WRITE = "write"
    INSTALL = "install"
    PROGRAM = "program"
    FIRMWARE_UPDATE = "firmware-update"
    RECOVERY = "recovery"


DESTRUCTIVE = frozenset({
    Operation.WRITE,
    Operation.INSTALL,
    Operation.PROGRAM,
    Operation.FIRMWARE_UPDATE,
    Operation.RECOVERY,
})


class OperationDenied(PermissionError):
    pass


def authorize(operation: Operation, *, explicitly_confirmed: bool = False,
              policy_enabled: bool = False) -> None:
    """Deny modifying operations unless both policy and per-action consent exist."""
    if operation in DESTRUCTIVE and not (policy_enabled and explicitly_confirmed):
        raise OperationDenied(
            f"{operation.value} denied: policy must be enabled and action explicitly confirmed"
        )
