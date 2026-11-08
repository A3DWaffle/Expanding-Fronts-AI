# LAND attack composition and loss recovery

This update applies to ordinary TL3/TL4 LAND ground lineups above 50 population. It keeps AIR, SEA, WATER, HYBRID, ASTEROID, early raids, and the monument modes on their existing composition/recovery rules.

## A useful core before launching

Regular attack requests and new Town Size Attack starts need four completed core units that can conservatively be counted outside the attacking army:

| Lineup | TL3 core | TL4 core |
|---|---|---|
| Troop / Troop with Heavy Weapons | Troopers or Mounted Troopers | Troopers or Mounted Troopers |
| Strike with Heavy Weapons | Strike Mechs | Strike Mechs |
| Mechball | Strike Mechs | Mech Destroyers |
| Deathball | Strike Mechs | Mech Destroyers or Assault Mechs |

For either/or requirements, four of one line qualify; mixed pairs are not summed. AA, transports, and other support units do not substitute for this core. The regular spare-batch requirements still apply: 8/11/16 defending soldiers for Rush/Aggressive/Defensive, aiming to commit about eight after personality allocation. The Fortress P2 siege requirement and military-strength hold remain independent.

AoC provides no per-type idle-unit counter here. The policy subtracts an upper bound on all attacking ground soldiers from the completed core count. For example, 1–4 attackers require eight owned core units to prove four spare. This can delay an attack when the deployed force mixes unit types, but does not count queued or deployed troops twice. It evaluates launch requests; it does not control the composition of every engine-created group during an active Town Size Attack. Separate Jedi pulses retain their composition behavior, but are blocked during recovery.

The TL4 LAND Strike lineup can maintain a minimum of eight Strike Mechs so small population settings can rebuild its spare core. The existing larger production targets remain in effect.

## Rebuild after a collapse

After observing at least eight attacking ground soldiers, the AI watches for the count to fall to two or fewer. This is a group-count loss estimate, not a casualty counter or local battle assessment. Disbanding or reassigning an attack can also trigger recovery.

Recovery closes new launches and automatic land attack-group formation, ends active Town Size Attack expansion, and leaves production and local defense running. It does not issue an explicit retreat command. It releases once the core is ready, the strength and Fortress holds clear, and the reserve reaches:

| Personality | 75/100 population | 125+ population |
|---|---:|---:|
| Rush | 8 | 16 |
| Aggressive | 11 | 22 |
| Defensive | 16 | 32 |

The larger reserve aims to commit about sixteen soldiers. A reserve already built can release recovery immediately. There is no fixed-time override that sends an understrength army. This depends on the economy being able to replenish the reserve and needs in-game testing, especially on Moderate. Recovery can trigger again after a later rebuilt attack reaches eight soldiers.

Debug messages remain bounded. Core shortages use the existing first WAIT/READY pair (`ATTACK GROUP: CORE LOW - WAIT`, then `ATTACK GROUP: READY`). Recovery adds one first-use pair per AI per match: `ATTACK GROUP: LOSSES - REGROUP`, then `ATTACK GROUP: REBUILT - READY`. Each is sent publicly and through local chat. These messages describe the relevant gate, not a guarantee that an attack launched.
