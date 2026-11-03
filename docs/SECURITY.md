# Security and safe operations

## Default-deny policy

Discovery, identification and read-only diagnostics are the initial safe scope. Any operation that writes, installs, programs, updates firmware or performs recovery must be explicitly enabled by policy and separately confirmed for that action.

## Required checks before a modifying operation

1. Identify the exact device, model and hardware revision.
2. Confirm the protocol and firmware version are in the driver's tested compatibility range.
3. Check power, cable, connection stability and required permissions.
4. Verify the origin, integrity and compatibility of any package or firmware image.
5. Make and verify a backup where the device permits it.
6. Explain the expected result and failure/recovery path.
7. Require explicit user confirmation immediately before execution.

## Logging and privacy

- Do not log Bluetooth addresses, serial numbers, Wi-Fi credentials or payload contents by default.
- Redact identifiers in diagnostic exports.
- Keep logs local and provide a clear retention/erase policy.
- Never send device data to a remote service without explicit opt-in.

## Physical interfaces

JTAG, SWD, UART and USB debug interfaces can expose sensitive device memory or alter boot state. They must be treated as advanced operations and remain unavailable unless a compatible probe, driver and documented procedure are selected.
