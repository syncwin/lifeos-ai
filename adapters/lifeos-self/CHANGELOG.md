# Changelog

## [0.6.0] - 2026-11-21

Breaking: the plugin `lifeos-selfos` is renamed `lifeos-self`, and its skills are renamed to match (`lifeos-selfos` is now `lifeos-self`, `lifeos-selfos-<stage>` is now `lifeos-self-<stage>`). Uninstall `lifeos-selfos` and install `lifeos-self`. Behaviour is unchanged. The plugin still needs the core `lifeos` plugin, which now holds the one LifeOS MCP connection (entity data is part of it).

## 0.5.2: 2026-11-23

**Changed**
- lifeos-verify agent: removed the undocumented `license` frontmatter key (directory gate D020).

## [0.5.1] - 2026-11-22

### Changed
- Version bump only, released together with the other LifeOS plugins.

## [0.5.0] - 2026-11-20

### Added
- First release as its own plugin, split from `lifeos` 0.4.0. Skills: `lifeos-selfos`, `lifeos-selfos-tasks`, `lifeos-selfos-reminders`, `lifeos-selfos-routines`.
- `references/`: copies of the core shared rules this module reads (kept in sync by a maintainer script, not shipped).

### Changed
- Needs the core `lifeos` plugin for the MCP connection and shared rules; the starter skills say so and stop when its tools are missing.
- Pointers to shared rules now resolve inside this plugin.
