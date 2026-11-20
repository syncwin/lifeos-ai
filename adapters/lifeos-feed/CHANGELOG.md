# Changelog

## [0.5.0] - 2026-11-20

### Added
- First release as its own plugin, split from `lifeos` 0.4.0. Skills: `lifeos-feed`.
- `references/`: copies of the core shared rules this module reads (kept in sync by a maintainer script, not shipped).

### Changed
- Needs the core `lifeos` plugin for the MCP connection and shared rules; the starter skills say so and stop when its tools are missing.
- Pointers to shared rules now resolve inside this plugin.
