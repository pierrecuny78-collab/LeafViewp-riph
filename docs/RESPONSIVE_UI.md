# Responsive UI and LeafBranding integration

LeafViewpériph is currently a Python core/CLI project. This document defines the requirements for any future desktop or Android graphical front end; it does not claim that a GUI already exists.

## Shared identity
Use the LeafBranding tokens in [LEAF_BRANDING.md](LEAF_BRANDING.md): Oasis #206B4D, Walnut #6B4935, Natural Gold #C5A46D, Cream #DCCBB1 and Sand Border #B69A7B. Show the LeafVibe identity and the LeafViewpériph product name in the app shell when the platform allows it.

## Adaptive layouts
- Phone (<600 dp): single-column device list, compact filters, device details on a separate screen or bottom sheet.
- Tablet (600–839 dp): list plus details when space allows.
- Wide (840–1199 dp): persistent navigation and split list/detail panes.
- Very wide (>=1200 dp): multi-pane workspace; up to five summary cards across only when labels remain readable.

Never rotate labels vertically to force a fit. Wrap or truncate with an accessible full-label alternative. Keep transport state, capabilities and safety actions distinct. No horizontal overflow, clipped controls or overlapping text. Touch targets must remain comfortable on mobile.

## Device workflow safety
Discovery and read-only diagnostics must remain distinct from writes, firmware flashing and recovery. Advanced/destructive actions require an explicit confirmation and capability check. Responsive layout must never hide or weaken those safeguards.

## Validation
Test narrow Android screens, landscape, tablet and desktop window resizing. Verify keyboard navigation, screen-reader labels, text scaling, scroll behavior and empty/error states.
