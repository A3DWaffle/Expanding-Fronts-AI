# Attack setting ownership

`groups.per` owns ordinary launch commitment percentages. `attack.per` loads it at the original execution position, after readiness vetoes and immediately before ordinary attack execution. Its order is personality defaults, WATER ground-wave commitment, then naval fleet commitment. It creates no attack requests and owns no timers or goals.

Other settings have distinct owners and scopes:

| Owner | Responsibility |
|---|---|
| groups.per | Ordinary ground/air/boat commitment percentages |
| ground.per | Shared ground release state and direct-pulse permission, recomputed after current core/recovery facts |
| attack.per | Readiness, launch execution, strength/siege/recovery holds, active TSA radius |
| sn-homebase.per | Normal town radius when TSA is inactive |
| sn-soldiers.per | Ground-group bounds and combat posture |
| combat-arm.per / shipyard.per | Naval groups and transport support |
| init-goals.per / attack.per | Explicit TL1 recall and separate opening/Jedi pulse exceptions |

Special-mode scripts retain their separate behavior. Do not move percentage settings ahead of readiness checks or after `attack-now`; that changes which units the engine commits. Do not introduce an unconditional town-radius writer alongside the active TSA owner.

The shared release states are BYPASS, GATHERING, READY, REBUILDING, CORE-LOW, HELD, and COMMITTED. Ground readiness uses goals 65–66 and no new timer. Normal late LAND/HYBRID ground lineups retain personality-specific reserves, core checks, and existing holds; WATER retains its full-wave threshold and fleet/air independence. Early raids, non-WATER AIR/SEA lineups, and ASTEROID retain their existing scope. Ordinary ground vetoes, WATER commitments, and Master pulses consume the shared result. A Master pulse marks COMMITTED and consumes its permission, preventing ordinary ground execution from using the same permission again that pass. WATER may still follow with fleet/air only. Waiting does not consume the pending Master request. No explicit recall is introduced.

Run `python -m unittest discover -s tests -v` from this repository with Python 3. The tests use only the standard library and check ordinary ownership, include placement, engine rule budgets, personality allocations, WATER ground readiness, fleet overrides, and absence of repeated commitment after a launch consumes readiness. These are supplied-state script tests, not engine movement or transport tests.

The initial `groups` extraction reproduced every original expanded attack rule in order without changing behavior. The subsequent shared-readiness improvement deliberately gates direct Master pulses and prevents repeated ground commitments in one pass. Existing production targets, fleet/air allocation, and ordinary batch thresholds are retained.
