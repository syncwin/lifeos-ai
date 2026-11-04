# Risk check
Fill this block in chat before every risky action, then wait. Only the exact reply below counts as a yes. Do not act on a vague "ok" or "sure".

```
RISK CHECK
What:       <the single action, in plain words>
Where:      <exact path, account, record or recipient>
Reaches:    <everything it touches: files, people, records, money, devices>
Why risky:  <what could go wrong>
Safer way:  <read-only, dry run, copy first, smaller batch, or draft only>
Undo:       <how to reverse it, or "cannot be undone">
Reply "go ahead: <What, 5 words max>" to proceed, or "no" to stop.
```

One block per action. A new action, target or batch needs a new block. A yes covers only what the block named.

## Actions that need it
| Action | Needs the block | Extra rule |
|---|---|---|
| Restore from backup, run a restore test | Yes | Restore to a new folder, never over live files |
| Move, rename or organise files | Yes | Show the full move list; moves go to the holding folder from the file rules, never straight to deletion |
| Delete, empty, overwrite | Yes | Offer the holding folder first; permanent deletion is the owner's own step |
| Money: payment, transfer, trade, saving an expense or bill record | Yes | Never move money or give financial advice; hand the action to the owner |
| Outbound message: email, chat, invite, post, reminder that notifies someone | Yes | Show the exact text and recipients |
| Reply or status sent back to a requester | Yes | Same as outbound message |
| New scheduled task or automation | Yes | Show the plan; run nothing hidden |
| Write to EntityOS (store or change an owner fact) | Yes | The write hook also asks |
| Read-only look, search, report | No | |
