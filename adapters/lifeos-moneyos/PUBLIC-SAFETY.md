# Public Safety

This repository is public. Only what is listed under "May be public" is published.

## May be public
- Skills, recipes and Markdown docs; maintainer script and hook sources under `dev/`
- Documentation, README, CHANGELOG, LICENSE
- Generic examples with placeholder values, `.env.example` (variable names only)
- The plugin's public support address `support@syncwin.com` (a published contact, allowlisted)

## Never published
- Secrets: API keys, tokens, passwords, private keys, `.env` files, credentials
- Personal data: personal e-mails, phone numbers, addresses
- Client names and data; internal URLs and hosts
- Local absolute user paths; private notes, logs, memory or progress files

## Where private values live instead
- This plugin has no options and holds no connection. The EntityOS endpoint URL and access token are options of the core `lifeos` plugin, stored locally as a sensitive setting and never written to a file in this repository.

## Checks
- `python dev/aiaddon-review/scripts/scan_secrets.py . --history` (working tree plus full git history, run with the aiaddon checker scripts) before every release
- Allowed false positives: `.public-safety-allow`, one entry for an old history hit that is not a credential

## If something leaks
Rotate the credential first, then remove it from history. Never force-push without the owner's explicit OK.
