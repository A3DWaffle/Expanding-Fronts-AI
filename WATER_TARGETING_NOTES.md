# WATER target selection

WATER now uses the engine's ordinary target evaluation with intelligent attacks enabled (`sn-attack-intelligence 1`) and reactions to incoming fire allowed (`sn-ignore-attack-group-under-attack 0`). Every script pass clears special target slot 2 to `-1` with influence `0`. The worker-memory TL1 commitment exception does not apply to WATER.

The shared worker/TL4 object preference rules explicitly exclude WATER. Previously, fleets and landing troops inherited maximum-influence preferences for workers, Assault Mechs, Artillery, aircraft, AA buildings, or Power Cores. TL4 could also retain the previous preference after all qualifying priority targets disappeared. Those preferences remain unchanged on LAND, HYBRID, and ASTEROID.

Special target slot 2 is a global object preference, not a boat-only targeting mode. Giving it a warship object instead would also bias landing troops. This repair removes that forced preference on WATER without selecting an enemy player, adding hidden-unit queries, or changing fleet production, transport assignment, wave thresholds, or LAND attack gates. Objective behavior in special target slots 1 and 3 is retained.

`tools/test_water_targeting.py` executes the targeting rules with supplied observations across all tech levels, five difficulties, and population caps 25, 50, 250, and 1,000. It checks stale-setting removal, response settings despite recent worker sightings, and unchanged non-WATER target priorities. These checks do not simulate engine pathfinding, weapon eligibility, targeting latency, or prefab obstructions.

Use fresh WATER matches to compare ordinary naval opponents and the reported Gungan prefab layout. Observe fleets while enemy ships approach or fire during a journey toward shore. Test TL2, TL3, and TL4; remove the former preferred target and check that ships can acquire another target. Confirm transport loading/escorts and landing troops still operate. Also compare a LAND match with the same personality. Already-issued engine orders are not explicitly recalled by this change.
