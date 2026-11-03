import pytest

from leafviewperiph.security.policy import Operation, OperationDenied, authorize


def test_read_only_operations_are_available_without_elevation():
    authorize(Operation.DISCOVER)
    authorize(Operation.DIAGNOSE)
    authorize(Operation.READ)


@pytest.mark.parametrize("operation", [
    Operation.WRITE, Operation.INSTALL, Operation.PROGRAM,
    Operation.FIRMWARE_UPDATE, Operation.RECOVERY,
])
def test_modifying_operations_fail_closed(operation):
    with pytest.raises(OperationDenied):
        authorize(operation)
    with pytest.raises(OperationDenied):
        authorize(operation, explicitly_confirmed=True)
    with pytest.raises(OperationDenied):
        authorize(operation, policy_enabled=True)
    authorize(operation, explicitly_confirmed=True, policy_enabled=True)
