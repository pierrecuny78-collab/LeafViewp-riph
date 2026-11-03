# Architecture

## Layering

1. **Core** — neutral device model, registry, lifecycle and event coordination.
2. **Communication** — transport adapters for BLE, Bluetooth Classic, Wi-Fi, USB, serial and debug probes.
3. **Drivers** — device-family knowledge; drivers declare supported operations and tested firmware/hardware ranges.
4. **Operations** — discovery, identification, diagnostics, data transfer, installation, programming and recovery.
5. **Security** — permissions, explicit confirmation, operation audit and secret handling.
6. **Integrations** — stable local API contracts for LeafCore and LeafBridge.
7. **User interfaces** — Android bridge and desktop control panel.

## Discovery flow

`platform adapter → candidate device → identification → compatible driver → declared capabilities → permitted operation`

Unknown devices remain visible as unknown. A driver must never infer a destructive capability from a device name alone.

## Adapter contract

An adapter implements the asynchronous `TransportAdapter` protocol. Discovery must be read-only. Platform-specific dependencies are optional extras, not mandatory imports of the core package.

## Device profile

Every device profile should declare:
- manufacturer, model and hardware revision when known;
- transport and protocol;
- firmware versions actually tested;
- capabilities and known limitations;
- permissions and safety level;
- upstream references and licence notes;
- automated and manual test evidence.

## Offline-first

The core must work without network access. Online catalogues and updates are optional. Cache metadata and signed packages locally; do not require a cloud account for local discovery or diagnostics.

## Platform reality

Windows, Linux and macOS have different permission and driver models. Android must use Android APIs or a companion bridge for Bluetooth/USB access; desktop Python libraries are not assumed to work unchanged on Android. JTAG/SWD requires compatible physical probes and drivers.
