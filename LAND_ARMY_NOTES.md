# LAND attack composition and loss recovery

Normal LAND/HYBRID ground strategies now also set the engine's minimum ground attack-group size to the package's intended committed wave (`land-wave-rush`) from TL3 onward, with a maximum of `land-rebuild-rush`. At 250 population these bounds are 8–16. Personality-specific at-home reserve checks still apply separately. This covers formation of new groups, including new TSA groups; it does not guarantee that later reinforcements, survivors, or scouts travel together. Early raids, non-WATER AIR/SEA strategies, and ASTEROID retain their group-size settings. WATER now has a separate ground commitment policy described in WATER_TARGETING_NOTES.md. Engine behavior requires fresh-match verification.

This update applies to ordinary TL3/TL4 LAND ground lineups at every supported population cap, 25 through 1,000. It keeps AIR, SEA, WATER, HYBRID, ASTEROID, early raids, and the monument modes on their existing composition/recovery rules. Shared LAND/HYBRID launch batching now also uses population-package targets.

## A useful core before launching

Regular attack requests and new Town Size Attack starts need a package-sized completed core that can conservatively be counted outside the attacking army:

| Lineup | TL3 core | TL4 core |
|---|---|---|
| Troop / Troop with Heavy Weapons | Troopers or Mounted Troopers | Troopers or Mounted Troopers |
| Strike with Heavy Weapons | Strike Mechs | Strike Mechs |
| Mechball | Strike Mechs | Mech Destroyers |
| Deathball | Strike Mechs | Mech Destroyers or Assault Mechs |

For either/or requirements, the required number of one line qualifies; mixed pairs are not summed. AA, transports, and other support units do not substitute for this core. The spare batch, core, production floor, loss trigger, and recovery reserve are defined in every population branch of both military population files, derived from that package's `MIL_POP_B`. Personality allocation adjusts the reserve needed to commit the intended wave. The Fortress P2 siege requirement and military-strength hold remain independent.

| Population cap | Required core | Intended normal wave | Intended rebuilt wave |
|---|---:|---:|---:|
| 25 | 1 | 2 | 2 |
| 100 | 2 | 3 | 6 |
| 250 | 4 | 8 | 16 |
| 1,000 | 16 | 32 | 64 |

These are intended committed soldiers, not total troops at home: Aggressive requires the ceiling of wave / 0.75, Defensive wave / 0.5. At 250 population that is 8/11/16 for normal waves and 16/22/32 after a collapse. All 40 cap options have explicit values in each of the two package files. TL2 batching uses a smaller package target, six intended soldiers at 250 population.

AoC provides no per-type idle-unit counter here. The policy subtracts an upper bound on all attacking ground soldiers from the completed core count. Counts of 0–4 attackers are exact; larger counts use conservative bands. At 250 population, one attacker requires five owned core units to prove four spare. This can delay an attack when the deployed force mixes unit types, but does not count queued or deployed troops twice. It evaluates launch requests; it does not control the composition of every engine-created group during an active Town Size Attack. Separate Master pulses retain their full-ground commitment, but now share the batch, core, siege, strength, and recovery release decision. A direct pulse consumes that scan's ground permission.

The TL3 LAND mech lineups and TL4 LAND Strike lineup can maintain twice their package core requirement, so they can rebuild a spare core. Existing larger production targets remain in effect. The old fixed TL3 composition rules are retained for other map modes and AIR; they cannot override the scaled LAND thresholds.

## Rebuild after a collapse

After observing an attacking ground force at least as large as its package wave, the AI watches for the count to fall to one quarter of that wave, rounded down. At 250 population this is eight falling to two; at 1,000 it is 32 falling to eight. This is a group-count loss estimate, not a casualty counter or local battle assessment. Disbanding or reassigning an attack can also trigger recovery.

Recovery closes new launches and automatic land attack-group formation, ends active Town Size Attack expansion, and leaves production and local defense running. It does not issue an explicit retreat command. It releases once the core is ready, the strength and Fortress holds clear, and the package recovery reserve is available. A reserve already built can release recovery immediately. There is no fixed-time override that sends an understrength army. This depends on the economy being able to replenish the reserve and needs in-game testing, especially on Moderate. Recovery rearms when a later attack reaches its package wave size.

Debug messages remain bounded. Core shortages use the existing first WAIT/READY pair (`ATTACK GROUP: CORE LOW - WAIT`, then `ATTACK GROUP: READY`). Recovery adds one first-use pair per AI per match: `ATTACK GROUP: LOSSES - REGROUP`, then `ATTACK GROUP: REBUILT - READY`. Each is sent publicly and through local chat. These messages describe the relevant gate, not a guarantee that an attack launched.
