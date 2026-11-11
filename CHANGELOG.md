# Changelog

Last verified: November 10, 2026. Current notes include Aggressive initiating TL2 attacks, warship priority, the TL2/TL3 Laser/Mounted ratio, delayed mech/Jedi responses, and town-clearing Pummels.

This file tracks major public-facing changes to the Expanding Fronts AI scripting project.

## 2026-11-09 - Aggressive can attack first

- Removed Aggressive's TL2 requirement to be attacked before it can launch. It can now initiate attacks using its normal readiness checks.
- Army minimums, batch checks, cooldown, treaty permission, and automatic/manual/scenario holds still apply. Defensive's TL2 attack hold is retained.

## 2026-11-09 - Warships before fishing expansion

- WATER/HYBRID combat-boat requests now run before transports, naval upgrades, and fishing boats. This prevents the early WATER trawler request and fishing expansion from always taking the first available Shipyard opportunity.
- TL2 combat boats no longer require fish to be present. HYBRID can request its first military Shipyard from TL2 without meeting fishing-economy thresholds, while still requiring Carbon Processing, Power, affordability, and the normal construction/raid gates.
- Fishing no longer depends on the legacy fishing/attack turn flag, which could remain stuck after the combat fleet filled its caps or became unavailable.
- Existing fishing and military unit caps remain unchanged. Trawlers can use remaining production when combat boats cannot train or have met their targets; this does not cancel already queued boats or guarantee simultaneous production in separate Shipyards.
- Rule tests cover WATER/HYBRID at TL2-TL4, every personality, no-fish maps, emergency naval AA, fishing fallback, and HYBRID's first Shipyard. Native resource timing, power placement, and fleet movement still require playtesting.

## 2026-11-09 - Laser Troopers before Mounted support

- TL2/TL3 Mounted Trooper orders now require two completed Laser Troopers per Mounted Trooper after the new order. Existing and queued Mounties count toward the limit; queued Lasers do not qualify. Only one Mounted order is requested per scan, and Laser losses pause new Mounties until the ratio is restored.
- Mounted upgrades wait for completed Lasers to satisfy both that ratio and the age/map P2 Laser core. TL3 Mounted-support lineups can train and upgrade their Laser core without requiring Repeater support; their first core tier need not wait for a Strike Mech.
- Removed TL2 rush Laser prerequisites that waited for Mounted counts, making support depend on the Laser core in one direction. Existing unit caps remain, and TL1 scouting/TL4 Mounted packages retain their earlier behavior.
- Seven focused rule tests pass, including queued units, loss recovery, upgrade gates, all map variants, existing package bounds, and affected rule sizes. Native production timing and defensive movement still require playtesting.

## Counter response reliability — November 9, 2026

- TL3 mech pressure prioritizes capped Bombers over Fighters, including P3/P4 alerts.
- Added delayed mech estimates on the existing Jedi intelligence clock; published Jedi warnings refill capped Hunter targets.
- Restored a bounded Pummel package for enemy buildings detected within the current town radius. See COUNTER_RESPONSE_NOTES.md for engine limits and validation.

## 2026-11-09

- Shared ground readiness now supplies ordinary batch vetoes, WATER ground commitments, and direct Master pulses. Pending Master requests wait for a proper batch and existing holds; a direct pulse consumes its permission so ordinary ground execution cannot reuse it in the same scan. Fleet/air independence and existing production targets are retained.
- Centralized ordinary ground/air/fleet commitment percentages in `groups.per`, included at their original execution position. Added standard-library regression tests in `tests/` and documented attack-setting ownership. Expanded attack rules retain identical conditions, actions, and order.
- WATER holds undersized ground commitments independently of fleet/air launches and commits ready ground waves together. Removed its continuous compact-town clamp, which fought normal and TSA radius changes every scan. Transport assignment and existing ground production quotas remain unchanged; engine movement and loading still need playtesting.
- TL3/TL4 LAND/HYBRID ground strategies set engine attack-group minimums from their population-scaled committed wave, with a matching larger maximum. Existing launch reserves remain independent; WATER sealift and early raids are unchanged.
- Low/guard Interceptor production follows the Attacker core; DANGER retains emergency priority. AIR lineups can rebuild to their full Attacker target after Fighter cover is satisfied, even with troop sightings. Fighter rules and aircraft target counts are unchanged.
- WATER no longer inherits forced worker, ground, or aircraft targeting preferences. Its attacks retain intelligent targeting and reactions to incoming fire.
- Every WATER personality builds a Spaceport followed by a War Center and completes both before TL3. Defensive's turret-first construction hold does not delay this pair.
- Unmarked maps default to LAND and fall back to HYBRID when fish or aquatic carbon vents are present. Explicit map objects retain priority; WATER and ASTEROID require those objects.
- Source and prototype scripts are synchronized. Script-level targeting, map-detection, and advancement checks pass; fresh-match playtesting remains necessary.

## Unreleased

- Added public repository structure.
- Added README documentation.
- Added `.gitignore`.
- Added prototype `.per` AI script files.
- Added notes explaining the project purpose, status, and file format.

## Notes

This project is currently prototype AI work. Some behavior may still be experimental, incomplete, or undergoing reorganization.
