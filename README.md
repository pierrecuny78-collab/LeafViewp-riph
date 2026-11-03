# LeafViewpériph

**LeafViewpériph** is the peripheral-management layer of the LeafVibe ecosystem. It is designed to discover, identify, describe, diagnose and communicate with supported devices through pluggable, capability-declared adapters.

> **Project status: initial scaffold.** This repository now establishes the architecture, a small Python core and automated tests. Real hardware support is not implied until an adapter has been implemented and tested on the target device.

## Goals

- Local-first and offline-capable operation.
- Device hot-plug and connection lifecycle management.
- Bluetooth Classic, BLE, Wi-Fi, Wi-Fi Direct, USB, USB-serial and supported debug interfaces through dedicated adapters.
- Explicit capability declarations: never assume a device supports an operation.
- Safe separation between discovery, normal operations and advanced firmware/debug operations.
- Integration contracts for LeafCore and LeafBridge.
- Windows, Linux and macOS as desktop targets; Android support through platform-specific bridges/adapters.
- Reusable open-source components only when their licences and redistribution terms permit it.

## Repository map

```text
src/leafviewperiph/
  core/            device models, registry, manager
  communication/   transport contracts and adapters
  drivers/          device-family drivers
  security/         policy and operation gates
  integrations/     LeafCore / LeafBridge contracts
  cli.py            diagnostic CLI
devices/            device profiles and compatibility records
docs/               architecture, security, compatibility, roadmap
tests/              offline unit tests
```

## Quick start

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\\Scripts\\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
leafviewperiph list
```

Optional transport dependencies are installed separately, for example:

```bash
python -m pip install -e ".[ble]"
```

## Safety model

- Discovery and read-only diagnostics are separate from writes, flashing and recovery.
- Every adapter declares its supported capabilities.
- Destructive operations are denied by default and require an explicit policy decision.
- No firmware image is bundled or automatically flashed.
- Device identifiers and personal data must not be logged by default.
- Unknown devices are reported as unknown; the system must not guess a driver.

## Compatibility status

See [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md). A listed upstream project is a research candidate, not proof that a particular peripheral or operation works.

## Licence

Original LeafViewpériph code is MIT-licensed. Third-party projects retain their own licences and notices; see [NOTICE.md](NOTICE.md). The MIT licence does not grant rights to proprietary firmware, vendor SDKs or trademarks.
