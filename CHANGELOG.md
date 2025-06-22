# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2025-mm-dd

### Added

- Deployed online documentation: https://flet-dev.github.io/flet-map/
- New controls:
  - `SourceAttribution`
  - `ImageSourceAttribution`
- New types:
  - `Camera`
  - `CameraFit`
  - `CursorKeyboardRotationConfiguration`
  - `CursorRotationBehaviour`
  - `KeyboardConfiguration`



### Changed

- Refactored all controls to use `@flet.control` dataclass-style definition.
- The following classes were renamed:
  - `MapInteractionConfiguration` → `InteractionConfiguration`
  - `MapInteractiveFlag` → `InteractionFlag`
  - `MapMultiFingerGesture` → `MultiFingerGesture`
  - `MapTileLayerEvictErrorTileStrategy` → `TileLayerEvictErrorTileStrategy`

## [0.1.0] - 2025-01-15

Initial release.


[Unreleased]: https://github.com/flet-dev/flet-map/compare/0.1.0...HEAD

[0.1.0]: https://github.com/flet-dev/flet-map/releases/tag/0.1.0