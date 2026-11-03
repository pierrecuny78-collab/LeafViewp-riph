# Roadmap

## Phase 0 — repository foundation
- [x] Establish package layout and contribution/licence policy.
- [x] Add device model, in-memory registry and fail-closed operation policy.
- [x] Add offline unit tests.
- [ ] Run CI on Windows, Linux and macOS.

## Phase 1 — discovery foundations
- [ ] Platform capability detection.
- [ ] BLE discovery adapter using optional Bleak dependency.
- [ ] USB and serial discovery adapters.
- [ ] Device identity and duplicate-resolution rules.
- [ ] Hot-plug event model.

## Phase 2 — device drivers
- [ ] Generic Android device profile.
- [ ] LeafWatch bridge adapter.
- [ ] Common USB storage and serial devices.
- [ ] Electronics board/probe profiles with hardware-specific tests.

## Phase 3 — operations
- [ ] Read-only diagnostics and connection health.
- [ ] Secure file/data transfer.
- [ ] Installer and local package catalogue.
- [ ] Backup/restore.
- [ ] Advanced programming and recovery only after safety review.

## Phase 4 — LeafVibe integration
- [ ] Stable local API for LeafCore.
- [ ] LeafBridge integration.
- [ ] Android and desktop user interfaces.
- [ ] Offline package and driver catalogue.
