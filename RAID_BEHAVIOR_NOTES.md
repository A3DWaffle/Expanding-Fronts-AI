# Current raid and TL2 behavior changes

The active source is **Expanding-Fronts-AI**. Its normal loader continues to use
the existing installed **Computer Prototype** name and folder. The separate
Computer Raid Prototype was an earlier staging copy; do not use it for testing
these current changes.

The current sync includes all 56 source modules in the installed Computer
Prototype and verifies their hashes against the source. The game archive is
also checked against the packaged source. A fresh-match engine test is still
required; file synchronization does not establish gameplay results.

## Attack signal and memory

`town-under-attack` refreshes `raid-attack-memory` to six heartbeat ticks on
every scan where it is true. Each tick is five game seconds, so the memory lasts
approximately 25–30 seconds after the last true observation. We have not yet
verified whether this engine reports shots on mounted raiders away from home
through this fact. The implementation uses the signal without assuming it is
restricted to the home base.

Visible enemy workers refresh a separate three-tick memory (about 10–15 seconds).
It uses `players-unit-type-count`, not an omniscient query. Negative results are
logged and do not count as sightings.

For a TL1 attacking group, request defense when **attack memory is active AND
worker memory is empty**. Block new TL1 launches under that same condition. A
raid with no attack signal is not recalled just because no workers were seen.
The previous independent raid grace timeout is removed. Native group response
is enabled without worker memory; recent workers permit continuing the raid.
Whether zeroing attack groups actually recalls already committed units still
needs an engine test.

The building pause separately lasts 30 seconds after a true attack signal. YES
and its post-timeout state now use different numeric values; brief signal loss
cannot prematurely clear the initial pause. After expiry, construction resumes
even if the signal remains true. A cleared signal rearms the next pause.

## Other changes carried into the active source

- Defensive completes three laser turrets before other production/tech expansion.
  Eight builders are requested for all seven installed turret-family IDs
  (79, 234, 235, 3599, 3600, 3601, 7088); the request returns to five afterward.
  All three personalities request at least five laser-turret builders from TL2
  onward, including the shared builder settings used after age transitions.
  Essential power, shelters and resource drop-offs remain available. Existing
  farm prerequisites still require the Spaceport + Temple/Mech Factory spine.
- Mines build through ID 5081 and also check spawned unit ID 5075, stopping
  requests at four live mine units belonging to this AI player. Detection uses
  `cc-players-unit-type-count` for the matching player slot (1–8); the old
  construction-object cap and native self unit-count check are removed.
  Requires more than 300
  spendable carbon. A three-tick cooldown spaces requests about 10–15 game
  seconds apart (five-second heartbeat). No resource refund; engine placement
  and spawned-unit counting still need a fresh-match test.
- TL1 age-up retains authorization for two Troop Centers and adds laser-line
  training up to the TL2 p1 target without the older worker-count/gremlin gates.
- Defensive rolls its mounted opening once at 50/50. In TL2 it trains the laser
  line up to the existing p4 target, without mounted dependencies; mounted/AA
  trooper production, scripted attacks and new scouts are disabled in that age.
- Aggressive trains the laser line in TL2 and can initiate attacks without
  first being attacked. Existing army/batch requirements, holds, treaty, and
  cooldown still apply.
- Rush uses the TL2/TL3 two-completed-Lasers-per-Mountie support ratio.
  Laser production no longer waits for Mounted counts.
- New scouts are blocked during attack memory, active attack groups and the
  active TL1 raid phase. Previously assigned scouts may continue.

## Diagnostics and validation

The recent RAID-DIAG chat messages are disabled, including repeated attack,
worker, pause, turret, mine and attack/recall diagnostics. Their chat actions
are replaced with `do-nothing`; policy actions and state transitions remain.

Use a fresh match to check changed rules; an existing replay does not test them.

Run `tools/test_raid_behavior.py` for offline state and structural checks.
The pre-integration source is backed up in
`tools/raid-prototype/main-before-integration.zip`. During integration, only the
anti-raid block of cheats.per was changed; existing resource-support differences
between the workspace and installed AI were preserved separately.


## External review repairs (2026-11-03)

Monument Race reconstruction, bounded raid-state recovery, and Aggressive
readiness corrections are now installed. See ../REVIEW_REPAIRS.md for the
reconstruction decisions, validation, preserved policies, and backups.
