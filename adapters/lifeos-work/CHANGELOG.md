# Changelog

## [0.6.0] - 2026-11-21

Breaking: the plugin `lifeos-workos` is renamed `lifeos-work`, and its skills are renamed to match (`lifeos-workos` is now `lifeos-work`, `lifeos-workos-<stage>` is now `lifeos-work-<stage>`). Uninstall `lifeos-workos` and install `lifeos-work`. Behaviour is unchanged. The plugin still needs the core `lifeos` plugin, which now holds the one LifeOS MCP connection (entity data is part of it).

## 0.5.2: 2026-11-23

**Changed**
- lifeos-verify agent: removed the undocumented `license` frontmatter key (directory gate D020).

## [0.5.1] - 2026-11-22

### Added
- `references/factory-workflow.md`: method for code or build tasks done by an agent; sprint and intake skills point to it.

## [0.5.0] - 2026-11-20

### Added
- First release as its own plugin, split from `lifeos` 0.4.0. Skills: `lifeos-workos`, `lifeos-workos-sprint`, `lifeos-workos-log`, `lifeos-workos-report`, `lifeos-workos-results`, `lifeos-workos-intake`, `lifeos-workos-demand`, `lifeos-workos-writing`, `lifeos-workos-research`, `lifeos-workos-brief`, `lifeos-workos-draft`, `lifeos-workos-review`.
- `references/`: copies of the core shared rules this module reads (kept in sync by a maintainer script, not shipped).

### Changed
- Needs the core `lifeos` plugin for the MCP connection and shared rules; the starter skills say so and stop when its tools are missing.
- Pointers to shared rules now resolve inside this plugin.
