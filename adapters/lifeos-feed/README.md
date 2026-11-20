# LifeOS Feed

The daily and on-demand feed of ranked, actionable cards. One of the LifeOS plugins; read the overview in the [lifeos-ai repository](https://github.com/syncwin/lifeos-ai).

**Version** 0.5.0 - **Author** SyncWin - **License** MIT

**Needs the core `lifeos` plugin.** The core holds the EntityOS MCP connection, the `/lifeos` router, the shared rules and the verify agent. This plugin has no connection or options of its own. If the core is missing or its tools are unavailable, the skills say so and stop.

**No personal data ships with it.** Every owner fact is read at run time from your own EntityOS endpoint through the core plugin.

## Install
```
claude plugin marketplace add syncwin/lifeos-ai
claude plugin install lifeos@syncwin-lifeos
claude plugin install lifeos-feed@syncwin-lifeos
```

## Skills
- `lifeos-feed`

## Layout
The plugin is text only: skills, a `references/` folder with the shared rules this module reads, and evals. The shared files are copies of the core's rules, kept in sync by a maintainer script in the repository that is not shipped.
