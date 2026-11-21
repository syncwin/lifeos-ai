# Changelog

## [0.6.0] - 2026-11-21

Breaking: the plugin `lifeos-entityos` is renamed `lifeos-entity`, and its skills are renamed to match (`lifeos-entityos` is now `lifeos-entity`). Uninstall `lifeos-entityos` and install `lifeos-entity`. Behaviour is unchanged. The plugin still needs the core `lifeos` plugin, which now holds the one LifeOS MCP connection (entity data is part of it).

## [0.5.0] - 2026-11-20

### Added
- First release as its own plugin, split from `lifeos` 0.4.0. Skills: `lifeos-entityos`.
- `references/`: copies of the core shared rules this module reads (kept in sync by a maintainer script, not shipped).

### Changed
- Needs the core `lifeos` plugin for the MCP connection and shared rules; the starter skills say so and stop when its tools are missing.
- Pointers to shared rules now resolve inside this plugin.
