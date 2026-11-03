# Compatibility and research register

This is a research shortlist, not a certification list. No hardware adapter is considered supported until it passes repeatable tests on a named device and firmware version.

| Component / project | Intended use | Licence / status | Integration decision |
|---|---|---|---|
| Bleak | Cross-platform BLE client | MIT; verify current upstream terms at pin time | Optional BLE adapter candidate |
| Gadgetbridge | Existing Android device support | AGPL-3.0; subcomponents may differ | Prefer protocol/interop study or isolated integration; legal review before code reuse |
| PyUSB | USB host access | Verify exact release licence and platform requirements | Optional USB adapter candidate |
| pySerial | Serial/UART access | BSD-style licence; verify upstream release | Optional serial adapter candidate |
| BlueZ | Linux Bluetooth stack | GPL-2.0; project-specific terms | System integration on Linux, not copied into core |
| Fit3 Toolkit / Fit3 Store | Galaxy Fit3 research and tooling | Verify repository licence and exact firmware scope before reuse | Research only; experimental |
| Fit3Free | Galaxy Fit3 BLE / GATT research | No clear licence identified in reviewed material | Do not copy code without permission |
| FitFace Studio | Watch-face editing | Verify exact licence and device/firmware support | Research only |

## Galaxy Fit3 (SM-R390)

LeafWatch is the dedicated project for Fit3 watch-side research. This repository should consume a documented LeafWatch bridge contract rather than duplicate its implementation.

Known constraints:
- The Fit3 is not a Wear OS watch.
- Do not assume arbitrary APK installation, general Linux access or a general-purpose filesystem.
- A tool tested in a simulator is not proof of real-watch support.
- Firmware modification and flashing remain out of scope until exact firmware matching, a verified recovery path and a safe test procedure exist.

## Status vocabulary

- **Research** — upstream or protocol investigation only.
- **Prototype** — code exists but has limited testing.
- **Tested** — repeatable test evidence exists for the named hardware/firmware.
- **Supported** — documented test matrix and maintenance owner exist.
- **Blocked** — licence, safety or technical blocker prevents integration.
