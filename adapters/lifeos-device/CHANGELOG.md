# Changelog

## [0.6.0] - 2026-11-21

Breaking: the plugin `lifeos-deviceos` is renamed `lifeos-device`, and its skills are renamed to match (`lifeos-deviceos` is now `lifeos-device`, `lifeos-deviceos-<stage>` is now `lifeos-device-<stage>`). Uninstall `lifeos-deviceos` and install `lifeos-device`. Behaviour is unchanged. The plugin still needs the core `lifeos` plugin, which now holds the one LifeOS MCP connection (entity data is part of it).

## [0.5.0] - 2026-11-20

### Added
- First release as its own plugin, split from `lifeos` 0.4.0. Skills: `lifeos-deviceos`, `lifeos-deviceos-health`, `lifeos-deviceos-backup`, `lifeos-deviceos-files`.
- `references/`: copies of the core shared rules this module reads (kept in sync by a maintainer script, not shipped).

### Changed
- Needs the core `lifeos` plugin for the MCP connection and shared rules; the starter skills say so and stop when its tools are missing.
- Pointers to shared rules now resolve inside this plugin.
