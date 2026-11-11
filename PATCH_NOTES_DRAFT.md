# Computer Prototype Patch Notes Draft

Last verified: November 10, 2026. Current notes include Aggressive initiating TL2 attacks, warship priority, the TL2/TL3 Laser/Mounted ratio, delayed mech/Jedi responses, and town-clearing Pummels.

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


## Current update - November 9, 2026

- **TL3 mech pressure gets a Bomber response before more Fighters.** When Bombers can train and are below their existing response target, they receive the next Airbase production opportunity. P3/P4 mech alerts now use the P2 Bomber package instead of falling through the old checks. The response no longer waits for a Fighter quota or the passive-age hold. Fighters resume once the Bomber target is met or Bombers cannot train.
- **Mech detection has a delayed fallback for unreliable visible counts.** Existing visible sightings still respond immediately where supported. The fallback checks the seven configured mech families, including Strike Mechs and the supported unique mech lines, on the existing intelligence clock: snapshots about 105 game seconds apart, published 45 seconds after capture. These total-count estimates can include hidden units. They merge with the existing five-minute mech memory without lowering a stronger remembered alert.
- **Jedi warnings replenish the capped Bounty Hunter response.** A nonzero published warning now permits replacements up to the existing Hunter target until a later NONE estimate replaces it. One order no longer consumes the warning, and the response no longer expires after 15 seconds. All Hunter response tiers can use food/carbon escrow. Jedi sampling remains delayed, includes Masters, Shadowtroopers, and alternate Temple Jedi, and does not track hidden changes between snapshots.
- **Pummels return as a small town-clearing package.** From TL3, enemy buildings detected inside the current town radius can trigger up to two Pummels including queued units, or one at 25 population, and one Heavy Weapons Factory if needed. Heavy Pummel research requires an existing Pummel and buildings in town. Production stops at the cap or when the buildings leave town; existing Pummels remain. During a Town Size Attack the radius may include offensive targets. Exact movement and building selection remain under native engine control.
- These are script and production-response changes. Automated checks cover supplied negative mech counts, delayed snapshots, Hunter replenishment, all population/difficulty packages, and capped Pummel requests. Native detection, pathfinding, and exact Pummel targeting still need fresh-match validation. Use the Steam archive AI; the separate Computer Diagnostics AI has been removed.


## Moderate Income Correction

* Restored the disabled main Moderate income block from the pre-export package; removed the accidentally reintroduced age grants, worker-band packets, reinforcements, and research-support income.
* Kept the 5-food TL1 worker support packet and all other baseline support exceptions. Hard/Hardest and the explicit Extreme override are unchanged.

## Hybrid AA Response

* Doubled AA Trooper constants across map variants, population caps, and difficulties; added TL2/TL3 Danger responses and raised the TL3 harassment floor from 3 to 6.
* Raised each enabled Hybrid fishing and warship cap by three in both difficulty tables. AA Destroyer package and alert targets now reach 7 boats at 250 population.
* Hybrid researches Heavy AA Destroyer in TL4 with at least one AA Destroyer and affordable, available research; WATER fleet thresholds and unrelated naval upgrade pacing no longer delay it.
* Hybrid AA Trooper and AA Mobile targets now match LAND for every population cap, difficulty, and faction branch, including all production stages.
* Hybrid's baseline TL4 AA Mobile rule now uses the same support-sam requirement as LAND. Interceptor responses already use shared LAND/Hybrid targets.

## Recent Eco and Forward-Base Pass - 2026-08-30

* Disabled forward Food Proc Ctr placement after testing showed it could place processors near enemy bases.
* Raised late Food Proc Ctr expansion caps: TL3 can now build up to 4 Food Proc Ctrs, and TL4 can build up to 5.
* Added late food-collapse recovery that forces TL3+ economies toward 70% food gathering when food falls below 300.
* Added escrowed late farm rebuild rules so TL3+ can spend small carbon banks on replacement farms before food production flatlines.
* Added a stronger TL4 farm recovery path after 3000 seconds, rebuilding toward 45 farms with up to 30 idle farm headroom.
* Farm layout cleanup now requires food above 300 before disabling farms, preventing cleanup from fighting starvation recovery.
* Late farm crisis construction now assigns 6 builders to farms when TL3+ food is below 300 and carbon is above 70.
* 250-pop Hard/Hardest land worker caps were raised from 88/105 to 96/115 for ally/no-ally games.
* TL4 Power Core overbuild was reduced: emergency Power Core cap is now 10, and rich forward Power Core support is capped at 8 instead of 22.
* Added rich TL4 forward Shield Generator starter support so forward bases can receive shields before the home shell reaches three shields.
* Added rich TL4 forward Laser Turret support capped at 14 total turrets.
* Added rich TL4 forward AA Battery support capped at 8 total batteries after the normal home battery shell exists.

  * 60001_ai_age-advancement.bin

    * Easy/Easiest no longer automatically force `age-match-human YES`.
    * TL2 age-up now requires 10+ workers, a Food Proc Ctr, and a Carbon Proc Ctr before researching.
    * TL3 age-up now waits at least 120 seconds in current age.
    * Config reset no longer restores Easy/Easiest age-match behavior.
    * Tech-disable toggle now restores normal teching to `age-match-human NO` when turned off.

* 60002_ai_aggressive.bin

  * Restored file.
  * AGGRESSIVE now assigns `openingstyle STYLE-AGGRESSIVE` when no personality was already selected.
  * AGGRESSIVE can initiate TL2 attacks without being attacked first, subject to normal launch checks; from TL3 it can also release its automatic hold once it has a small military force.
  * AGGRESSIVE uses lower attack thresholds than DEFENSIVE and steadier pacing than RUSH.
  * Retains the broad "standard computer" behavior but with less brute-force cheating and more strategy gating.

* 60003_ai_airbase.bin

  * Airbase tech handling moved back into this file.
  * DEFENSIVE opens TL3 with two airbases.
  * AGGRESSIVE and RUSH make an airbase later in TL3 to unlock cargo freighters.
  * Airbase count scales higher for AIR strategy or aircraft support.
  * Rich TL4 AIR/support-aircraft economies can add two more forward Airbases, capped at 6.
  * Air transports enabled for maps marked ASTEROID.
  * Aircraft production is gated by AIR strategy, support-aircraft, DEFENSIVE behavior, or relevant map support.
  * DEFENSIVE always trains Fighters and can train Bombers against mech pressure in TL3.
  * TL3 Fighter production remains default air response when bombers are not justified.
  * TL3/TL4 Fighter cover no longer waits on Attacker quotas before continuing production.
  * TL3/TL4 Fighter cover has small floor rules so low-pop quota packages do not stop at one Fighter.
  * TL4 air package prioritizes Attackers, then unlocks Interceptors, Fighters, and Bombers as quotas are met.
  * Bombers are delayed behind TL4 Attacker p4 progress so the AI spends nova on stronger air first.
  * Interceptor response was made easier to reach for AIR and aircraft-support plans.
  * Aircraft upgrades now check that the AI is using relevant aircraft.
  * Fighter upgrades have rich/late fallbacks based on actual Fighter presence.
  * New Republic New Class Modernization has a rich/late fallback when real air units exist.

* 60004_ai_animal.bin

  * Animal techs moved back into this file.
  * Acklay support is tied to the modern support selector.
  * Nexu are limited to RUSH in TL3.
  * Reeks are limited to RUSH after Acklay quota is met.
  * Probots and Vornskyrs were removed from the AI lineup.

* 60005_ai_attack.bin

  * Attack file now owns regular-game personality attack pacing, attack holds, TSA, ally join-ins, and special target behavior.
  * Important research goals can hold attacks until the AI is ready.
  * TL1 attacks no longer launch with only Trooper Recruits.
  * RUSH and DEFENSIVE TL1 pressure uses Mounted Troopers.
  * TL1/TL2 opening attacks roll a building target, heavily weighted toward Carbon Processing Centers.
  * TL1/TL2 attacks switch special target preference back to workers immediately after launch.
  * TL3 forces worker targeting and ends the opening building-target experiment.
  * TL2 rush thresholds now scale by rush size: SMOL 7, NORM 11, BIG 15 military population.
  * Hard can randomly stop TL2 rush pressure after the first wave; Hardest always continues.
  * TL2 attack rules use longer pacing instead of rapid 90-second pressure.
  * TL2 timer-triggered attack branches avoid stacking multiple attack-ready states in the same timer window.
  * TL2 AI ally join-ins are restricted to avoid attack-command loops.
  * AGGRESSIVE and DEFENSIVE TL2 now use the shared TL2 launcher instead of bypassing cooldown logic.
  * TSA selection now depends on modern population and military-population thresholds.
  * Max-pop attacks and TSA behavior were simplified around modern population thresholds.
  * Added pressure attacks at 25 military population to reduce idle army spacing issues before popcap.
  * Scenario attack holds and TL1 mounted pressure now respect treaty/hold ordering.
  * Center gather taunt behavior remains available for human commands.

* 60006_ai_building-count.bin

  * Building-count now focuses on builder assignment and building-count milestones.
  * TL1 uses one builder per key structure to avoid early worker overcommit.
  * TL1 food-crisis farms switch to 3 builders when food is low, carbon is available, and worker count is over 10.
  * TL2 builder counts stay lean: Mech Factory and Spaceport use 2 builders, farms use 2, and most secondary structures stay at 1.
  * TL3+ restores larger builder counts for faster construction.
  * TL3+ late food-collapse farms switch to 6 builders when food is below 300 and carbon is above 70.
  * Older broad strategic building-count behavior has been deprecated.

* 60007_ai_carbon.bin

  * Carbon file now handles Carbon Proc Ctrs and carbon-side economy techs.
  * Hunt openers can build the first Carbon Proc Ctr before the first Food Proc Ctr so the eco spine forms earlier.
  * Early Carbon Proc Ctr placement uses tighter carbon drop-site spacing and can trigger when carbon is more than 1 tile from an existing drop site.
  * First Carbon Proc Ctr waits for initial food infrastructure and avoids interrupting animal-saving behavior.
  * Added timeout fallback if the AI still has no Carbon Proc Ctr.
  * TL2+ Carbon Proc Ctr expansion uses distance checks and escrow.
  * Carbon-side economy techs are handled from this file.

* 60008_ai_cheats.bin

  * Cheats file now handles difficulty resource support, refunds, and build-order recovery.
  * AI cheat timer cadence was adjusted for the new opener/package logic.
  * Early worker food support remains for Moderate+ so worker production does not stall.
  * Hardest TL1 worker-band and stuck-age food support was reduced so age-up timing depends more on real food gathering.
  * Hard/Hardest TL2 routine nova cheat support was roughly halved while severe TL3 catch-up support remains intact.
  * Hardest routine TL2 carbon cheat packets were reduced while keeping severe catch-up support intact.
  * Moderate+ gets a delayed one-time TL1 carbon bridge only if the first Troop Center is still late.
  * TL1 carbon supports and early carbon refunds were reduced so early structure timing depends more on real gathering.
  * Refund goals are used for proc centers, power cores, shipyards, and other early infrastructure.
  * Cheat behavior is more targeted around build-order failures and resource shortfalls instead of broad constant income.
  * Under-attack build pause now briefly stops structure attempts, clears queued structure goals, then releases building again during long assaults.

* 60009_ai_civ-loads.bin

  * Added standardized header/comment structure.
  * Depreciated file.

* 60010_ai_combat-arm.bin

  * Added modern core combat-arm and support package selector.
  * AI rolls a core army plan from civ-specific matrices.
  * Support flags can layer multiple support roles on top of the older single support enum.
  * HYBRID maps now allow for small naval force.
  * ASTEROID maps now allow all civs to go air.
  * Civ matrices control support-aircraft, mounted, unique, artillery, master, and other support availability.

* 60011_ai_constants.bin

  * Added modern combat-arm and support package constants.
  * Added modern air, boat, mech, and Jedi alert ladders.
  * Added `enemymechsighted`, `enemyboatsighted`, and related detection counters.
  * Added `support-sea` separate from `support-sealift`.
  * Added `opening-attack-target` state for the TL1/TL2 target experiment.
  * Added branch/map constants for special maps and population packages.
  * Removed cheat sight detection for the AI, replaced with non-cheating and a memory of five minutes.
  * Removed active dependency on alternate building aliases in prototype logic.
  * Mech unique detection uses valid mech/anti-mech unit names and excludes invalid old entries.
  * Ten-minute pulse now coordinates late-game permissions for cannon, ore purchasing, scouting, Jedi/Master support, and holocron services.
  * Shared build-retry/refund states support proc centers, power cores, shipyards, heavy weapons, airbase, and mech factory recovery.

* 60013_ai_defensive.bin

  * DEFENSIVE now assigns `openingstyle STYLE-DEFENSIVE` when no personality was already selected.
  * DEFENSIVE keeps TL2 attacks on hold.
  * DEFENSIVE starts fighter trick behavior in TL3.
  * DEFENSIVE can release attack holds after building enough military population.
  * DEFENSIVE uses higher attack thresholds than RUSH or AGGRESSIVE.

* 60018_ai_diplomacy.bin

  * Removed large obsolete comment block from the reference file.
  * Keeps core diplomacy state mirroring and alliance/enemy behavior.
  * Retains teams-unlocked diplomacy behavior.
  * Added standardized header/comment structure.

* 60019_ai_fishboat.bin

  * File remains legacy-named but actually handles Advanced Infantry Center support.
  * Advanced Trooper caps now use modern `TL  *-trooper-core` constants.
  * Removed random junk-unit training from the Advanced Infantry Center.
  * Added standardized header/comment structure.

* 60020_ai_food.bin

  * Initial Food Proc Ctr timing now distinguishes berries, no-berries, and hunt maps.
  * Hunt openers force the first Food Proc Ctr by 120 seconds once a Carbon Proc Ctr exists, without using forward placement.
  * Hunt maps delay the first food proc briefly so early workers can use nearby hunt.
  * TL1 food-crisis fallback can build the first Food Proc Ctr earlier on failed hunt transitions.
  * Carbon-rich TL1 food-crisis economies can build a second Food Proc Ctr when remaining food is still far from existing drop sites.
  * TL2 hunt maps can build up to 3 total Food Proc Ctrs when food is low and remaining food is still distant.
  * Food Proc Ctrs no longer use forward placement because it can send them into enemy bases.
  * Added a TL1 hunt-food phase before deciding on extra food dropoffs.
  * TL1 hunt maps clamp `sn-mill-max-distance` after Food Proc Ctrs are up so workers prefer local food instead of edge animals.
  * TL2 hunt maps use tighter dropoff behavior to reduce overextension.
  * Food Proc Ctr expansion is capped more carefully in TL1.
  * Later Food Proc Ctr expansion uses distance and resource-state checks.
  * Late Food Proc Ctr expansion now reaches 4 total in TL3 and 5 total in TL4.
  * Food Proc Ctr placement now requires nearby food when food exists, with a no-food fallback so farms can still unlock.
  * Verified food-lure animals use the hunt economy path so boar hunt task groups can form without non-food lure classes breaking no-berry starts.

* 60021_ai_fortress.bin

  * Air Cruiser production is tied to AIR strategy or Aircraft support.
  * Cannon production follows modern combat-arm/support logic instead of old 1v1-specific caps.
  * Air Cruiser production now waits for late Attacker progress and basic Fighter cover so fortress nova is not spent too early.
  * TROOP and TROOP/HW can use more Cannons as late siege.
  * Fortress techs wait on important TL4 research where appropriate.
  * Fortress unique unit techs moved back into this file.
  * Unique-unit and cannon training use generated package constants.

* 60024_ai_heavy-weapons.bin

  * Heavy Weapons Factory now handles building, siege upgrades, and siege production packages in one file.
  * TL3 Heavy Weapons Factory construction is tied to artillery/HW strategy or support artillery needs.
  * TL4 Heavy Weapons Factory count scales higher for TROOP/HW, MECH/HW, ARTILLERY support, or support-artillery.
  * Rich TL4 artillery/HW economies can add extra forward Heavy Weapons Factories, capped at 5.
  * Artillery upgrades moved back into this file and wait for artillery/HW strategy or support.
  * Pummel/Ram training and upgrades now use the bounded town-clearing conditions in the current update above.
  * AA Mobile air-alert rules release escrow and briefly block ram/artillery training during GUARD/DANGER alerts until the LOW AA Mobile threshold is met.
  * TL3 missile and artillery production use staged p1/p2/p3 thresholds.
  * AA response thresholds were lowered for earlier reaction, then production caps were reduced one tier to avoid overcommitting.

* 60025_ai_homebase.bin

  * Homebase owns core base infrastructure: Command Centers, workers, prefabs, farms, power cores, and medics.
  * Command Center expansion scales through TL3/TL4 constants and late-game TSA pressure.
  * Worker production uses modern worker caps, water-map worker caps, and late-game worker trimming.
  * Prefab Shelter logic builds earlier and keeps larger housing headroom in TL2+.
  * Farm logic handles TL1 emergency food, berry/no-berry cases, hunt-map transitions, and TL2+ farm support.
  * No-berry hunt starts can add a safety farm after 4 minutes instead of waiting 10 minutes, reducing carbon overcommit on risky animal starts.
  * TL1/TL2 emergency farm support now reacts to high carbon with low food and 10+ workers.
  * TL1 carbon-glut recovery can build toward 10 farms when food is low and carbon is heavily banked.
  * TL2 adds an 8-farm floor after 18 workers so food income stabilizes before hunt fully expires.
  * TL3+ late food-collapse recovery re-enables farms, releases escrowed carbon, and rebuilds toward 30 farms when food is critically low.
  * TL4 late food-collapse recovery has a stronger hour-game rule that rebuilds toward 45 farms with up to 30 idle farm headroom.
  * Farm layout cleanup now requires a 300-food buffer before disabling farms, so cleanup does not fight starvation recovery.
  * Power Core construction supports TL1 spine building and larger TL2/TL4 power needs.
  * TL4 Power Core overbuild was reduced: emergency Power Core cap is now 10, and rich forward Power Core support is capped at 8.
  * Structure-building rules now use the shared timed `buildpause` gate so long assaults do not permanently freeze construction.
  * Remaining building alias references were restored to real `BLDG-  *` names.

* 60026_ai_init-goals.bin

  * Initializes shared goals expected by the current load chain.
  * Sets `tryingtobuild`, `get-mad`, and initial scaling SNs.
  * Disables difficulty scaling of strategic numbers.
  * Keeps `sn-scale-minimum-attack-group-size` disabled due attack group scaling issues.
  * Added standardized header/comment structure.

* 60027_ai_jedi-temple.bin

  * Jedi Temple handles temple construction, Jedi units, Jedi Masters, temple unique units, and temple techs.
  * Standard Jedi Temple is delayed until late TL3.
  * Added TL4 fallback Temple construction so the AI is not stranded behind unfinished TL3 important research.
  * Black Sun can no longer build an earlier temple through its special path.
  * Holocron collection trains a Jedi or Black Sun hunter and retries for a limited time.
  * Holocron collection gives up after long game time instead of trying forever.
  * Jedi Masters require Master support and sufficient military population before spending nova.
  * Temple unique units use combat/support flags.
  * Jedi and temple techs wait on relevant unit presence and important research timing.
  * Restored missing Temple research coverage. Faith in the Force and Force Purge get priority gates, while secondary Force upgrades wait until Masters are fielded.

* 60028_ai_map-loads.bin

  * Fish-heavy maps now set `special-map HYBRID` instead of always becoming WATER.
  * Vents alone no longer promote a map to WATER/HYBRID.
  * Only verified food-lure animals set `hunt-present YES` so boar task groups can form.
  * Low-lure-food detection preserves `allowgarbage LOWLUREFOOD` metadata while preventing non-food lure classes from blocking no-berry starts.
  * Several hardcoded map-special promotions were disabled with `do-nothing`.
  * Added clearer chapter structure for setup, map detection, resource detection, and special maps.

* 60030_ai_mech-factory.bin

  * Mech Factory handles building, mech upgrades, and mech production packages in one file.
  * TL2 Mech Factory bumped in build order so AI makes them first in TL2 alongside a spaceport.
  * TL3 Mech Factory construction is paced behind economy/building progress.
  * TL4 Mech Factory count scales higher when MECH, MECH/HW, Assault Mech support, or support-assault-mech is active.
  * Rich TL4 mech economies can add extra forward Mech Factories, capped at 8.
  * MECH and MECH/HW can add one extra late TL3 Mech Factory after Spaceport and War Center are online.
  * MECH and MECH/HW can add one extra TL4 Mech Factory after the existing fifth-factory stage.
  * Mech upgrades moved back into this file.
  * TL3 Strike Mechs priotized.
  * TL3 Mech Destroyers are tied to MECH strategy and mech detection pressure.
  * Wookiee Ingenuity now researches from the real Wookiee tech id when Wookiees field mechs, including Transport Mechs.
  * TL4 Mech production is staged by p1/p2/p3/p4 package thresholds.
  * Transport Mechs are treated as support tied to troop-style packages rather than generic mech spam.

* 60031_ai_military-population.bin

  * Normal-difficulty military population constants were expanded into generated package thresholds.
  * Added p1/p2/p3/p4 package thresholds for staged unit production.
  * Added water, asteroid, and hybrid branch variants for many packages.
  * Added detection-response constants for air, mech, Jedi, boats, and other support packages.
  * Added package constants for modern core-arm and support-unit selectors.
  * Added worker, cargo, fishing boat, and population pressure constants used by economy and production files.

* 60034_ai_nova.bin

  * Nova file now only handles nova processing and nova mining techs.
  * Ore processing logic moved out to the ore file.
  * TL1/TL2 Nova Proc Ctr construction requires carbon infrastructure and a Troop Center, and caps at 1 early proc.
  * TL3+ Nova Proc Ctr camplevel rules were split into smaller parser-safe rules.
  * Nova mining techs wait on important research timing.

* 60035_ai_ore.bin

  * Ore file is no longer empty.
  * Ore processing logic moved back into this file from nova.
  * DEFENSIVE builds an Ore Proc Ctr in TL1 as part of its opening.
  * DEFENSIVE can force an Ore Proc Ctr in TL2 once its basic economy is online.
  * Ore mining techs wait on important research timing.
  * Added fallback handling for maps where ore is too far away or runs out.
  * TL3+ Ore Proc Ctr camplevel rules were split into smaller parser-safe rules.

* 60036_ai_population.bin

  * Population file now has standardized documentation.
  * Keeps economic population, worker, trade, and pop-limit constants.
  * Retains failsafe population-cap chain behavior from the reference.
  * No major behavior rewrite beyond documentation/formatting in the current prototype diff.

* 60037_ai_randomgame.bin

  * Added `military-population` to always-loaded constants so lower difficulty package sizes are available.
  * Added `military-population-hard` for hard package sizes.
  * Added `combat-arm` to normal random-map setup so personality and army package rolls happen before production files load.
  * Added random personality overlay loading for AGGRESSIVE, DEFENSIVE, and RUSH.
  * Normal mode load order supports the split between core strategy, economy, research, and unit production files.
  * Monument Race and Defend the Monument load paths were updated to the new format.

* 60038_ai_research-center.bin

  * Research Center tech handling moved into this file.
  * First Research Center requires TL3 and 3 Command Centers.
  * Second Research Center remains a TL4 follow-up and caps the AI at 2.
  * Added Research Center core tech rules.
  * Added Research Center unique tech rules.
  * Tracking and Targeting Computers wait for important TL3 research.
  * TL4 economy/building techs wait for important TL4 research.
  * Defensive Research Center techs can be researched early by DEFENSIVE, or later by other personalities after important TL4 research.

* 60039_ai_research.bin

  * Research file was reduced from broad tech handling to shared non-unit upgrades and important tech checks.
  * Most unit-line techs moved out to their unit production files.
  * Important TL2/TL3/TL4 research is now driven by combat-arm and support bundles.
  * TROOP and TROOP/HW bundles require core trooper weapon/armor upgrades before unlocking important research.
  * MECH and MECH/HW bundles require core mech weapon/plating upgrades before unlocking important research.
  * SEA and support-aircraft bundles use lighter age-appropriate readiness checks so non-ground strategies are not stalled by irrelevant troop/mech techs.
  * TL4 readiness uses split availability-safe goal checks so unavailable faction techs do not block important research forever.
  * Shield Modifications prioritizes real air strategies and air unique units.
  * Sensor Beacon and Sensor Array require 3 Command Centers and important research timing.
  * Defensive structure techs remain here but are gated later behind important research.

* 60040_ai_rush.bin

  * Rush file is no longer empty/defunct.
  * RUSH sets `openingstyle STYLE-RUSH` if no personality was already assigned.
  * RUSH can resume attacks in TL2 once it reaches 6 military population.
  * RUSH pauses attacks in TL3 to recover and rebuild.
  * RUSH resumes normal attacks again in TL4.

* 60041_ai_shipyard.bin

  * First Shipyard requires a Troop Center and Power Core.
  * WATER and HYBRID maps set `support-sea YES`.
  * WATER maps set `support-sealift YES`; HYBRID does not, so hybrid maps do not train transports.
  * TL2 Shipyards wait for Mech Factory, Spaceport, Power Core, and important TL2 research.
  * TL3/4 Shipyards wait for either 3 Command Centers or 2 Airbases.
  * Shipyard placement now keeps docks closer to the base and avoids chasing distant fish.
  * Fifth TL4 Shipyard requires water support instead of old boat-civ assumptions.
  * Boat upgrades no longer wait on important TL4 unique research.
  * Fishing boat rules no longer stop just because the AI is close to population cap.
  * TL2 naval army centers on Frigates, with AA Destroyers only added when enemy air is detected.
  * TL3 naval production uses support-sea and builds staged Frigate, AA Destroyer, Destroyer, and Monitor packages.
  * TL4 naval production uses support-sea and builds staged Frigate, AA Destroyer, Destroyer, Cruiser, and Monitor packages.
  * Extra AA Destroyers scale from enemy air detection in TL2/3/4.
  * AT-AT Swimmer count uses the water unique-unit constant.

* 60042_ai_sn-gather.bin

  * Save-the-animals starts when any herdables are found instead of waiting for 3+.
  * Save-the-animals nursery build rules were split into smaller parser-safe rules.
  * RUSH and DEFENSIVE can build a late TL1 Animal Nursery if their opener missed one.
  * TL1 gather rates change by personality.
  * RUSH gathers about 3 workers on nova in TL1 after 20 workers and a Nova Proc Ctr.
  * DEFENSIVE gathers ore in TL1 after building an Ore Proc Ctr.
  * Standard TL1 play only gathers nova after 20 workers and an existing Nova Proc Ctr.
* TL2 ore gathering is synced across difficulties and capped lower so ore stays a small top-up resource.
* Generic TL2 worker mix is carbon-forward while the Mech Factory and Spaceport spine comes online, but keeps nova as a stronger normal gather lane.
* TL2-to-TL3 age-up now pivots to a 30/40/30 carbon/food/nova split and cuts ore so nova is ready for TL3 units and tech.
  * TL2 hunt maps keep more workers on food.
  * TL1/TL2 carbon-overflow food parity rules now push workers harder onto food when food is low and carbon is already banked.
  * TL1 high-carbon starvation override now runs after the normal spine rules so food recovery is not overwritten.
* RUSH TL2 gathers more carbon/food/nova and less ore.
  * DEFENSIVE TL2 gathers less ore while building turrets, keeping carbon and stronger nova income alive for the Mech Factory and Spaceport spine.
  * RUSH TL3 uses a custom recovery gather setup while attacks are on hold.
  * DEFENSIVE TL3 uses a custom food/nova gather setup.
  * TL3+ late food-collapse recovery forces 70% food gathering when food is below 300, even if carbon is also low.
  * Remaining building alias references were restored to real `BLDG-  *` names.

* 60043_ai_sn-homebase.bin

  * Initial maximum food drop distance increased from 12 to 14.
  * Initial hunt/lure targeting distance is held to 30 so boar task groups prefer nearby animals instead of edge targets.
  * Opening lure parties are blocked by setting minimum boar hunt group size to 99, then relaxed to 3 after 4 minutes.
  * Removed importantT4unique DONE checks from TL4 town-size expansion logic.
  * TL4 town-size expansion waits on importantT4research DONE before trying to make room for missing buildings.
  * Remaining building alias references were restored to real `BLDG-  *` names.

* 60044_ai_sn-soldiers.bin

  * Projectile dodge behavior disabled across difficulties by setting ability-to-dodge-missiles to 100.
  * TL3/4 maintain-distance behavior disabled by setting ability-to-maintain-distance to 100.
  * RUSH and DEFENSIVE can use the first mounted unit to aid scouting if an enemy Command Center has not been found.
  * `sn-task-ungrouped-soldiers` is still fought/reset by prototype rules.
  * Added persistent sentry-distance clamps:
    * TL2 max `14`.
    * TL3 max `16`.
    * TL4 max `18`.
  * Defense distance remains age-scaled separately from sentry distance.

* 60045_ai_spaceport.bin

  * Spaceport techs moved back to this file.
  * Confederacy Alliance, Piracy, and Cloaked Smuggling require an ally before research.
  * Commodity trading requires 3000+ stockpile before most trading rules activate.
  * Routine metal buying removed from small and medium trade rules.
  * DEFENSIVE can sell ore for nova if food/carbon are ready but nova blocks TL3.
  * TL4 metal buying requires stronger spare nova/food/carbon stockpiles.
  * Human tribute requires the AI to have 3000+ of the requested resource before sending tribute.
  * AI-to-AI tribute requires 3000+ of the donated resource before sending food, carbon, nova, or ore.
  * Spaceport-owned civ techs are handled in this file with escrow releases.

* 60046_ai_supplement.bin

  * Removed SCN unit logic for now because it used deprecated constants.
  * Retained a smaller compatibility supplement file.

* 60047_ai_tower.bin

  * Tower file controls defensive walls, turret behavior, and cleanup in one place.
  * Rich TL4 economies can forward-build extra Shield Generators once the home shield shell is established.
  * Rich TL4 forward Shield Generator starter support can protect a forward base once the AI has a fortress, five Power Cores, and sufficient stockpile.
  * Rich TL4 economies can forward-build additional Laser Turrets and AA Batteries once the forward-base economy is established.
  * Walls are disabled by default instead of being broadly available.
  * Defensive structure behavior is more tightly gated by personality and research timing.

* 60048_ai_troop-center.bin

  * TL1 Troop Center requires Power Core, Carbon Proc Ctr, and Food Proc Ctr.
  * First TL1 Troop Center can release escrowed carbon once the Power Core is placed so it lands with the opener spine.
  * TL1 Troop Center caps at 1 unless RUSH builds another while aging.
  * TL2 Troop Center requires Power Core, Mech Factory, and Spaceport; cap is 2.
  * TL3/4 Troop Center requires two airbases or two Command Centers.
  * TL3/4 Troop Center cap is 2 if troopers are not part of strategy, 5 if they are.
  * Rich TL4 troop economies can add extra forward Troop Centers, capped at 7.
  * Trooper unit-line upgrades are researched only if the AI is using relevant units.
  * RUSH and DEFENSIVE train TL1 mounties for pressure; TL1 recruits stay cheap at p1 unless the AI is already aging up.
  * AGGRESSIVE periodically trains trooper recruits for defense and avoids TL1 mounted pressure.
  * Mounted units train when Laser Trooper quotas are met, except DEFENSIVE skips TL2 mounties to preserve age-up resources.
  * Non-troop strategies stop broad trooper training except AA troopers.
  * TL3 single-air detection now maintains a 3-AA-Trooper floor so one camping aircraft does not stall the AI.
  * Grenade Troopers train once Laser Trooper quotas are met or mech pressure justifies them.
  * TL4 Laser Troopers train once artillery or grenade quotas are met.
  * Remaining building alias references were restored to real `BLDG-  *` names.

* 60049_ai_war-center.bin

  * War Center research moved back here.
  * AI only makes a War Center in TL2 if it is RUSH personality.
  * TL3 War Centers require either 2 airbases or 3 Command Centers.
  * War Center cap is 2.
  * War Center techs require the AI to field units that can benefit from the techs.
  * Targeting Sensor now recognizes Assault and Transport Mechs, with a rich/late mech fallback.
  * Zann can now research Grenadier Training without requiring a Grenadier support package. Assault Mechs also return to normal TL4 MECH and MECH/HW production, with all Assault Mech rules unlocked from p2 package progress instead of waiting on late-stage artillery or mech quotas.
  * TL4 age-up hard timed fallback now fires at 25 minutes instead of 28 minutes.
  * War Center techs moved to TL3+ unless RUSH.
  * Remaining building alias references were restored to real `BLDG-  *` names.

* 60050_ai_warboat-island.bin

  * Restored and cleaned dialogue behavior.
  * Large island/warboat dialogue script remains mostly intact with formatting and cleanup.

* 60051_ai_warboat.bin

  * Deprecated broad warboat behavior; shipyard now owns shipyard/naval production.
  * File now retains late-game utility hooks under the legacy warboat name.
  * Late cannon and Master support remain as utility behavior.
  * Removed large obsolete hard/hardest-only late-game blocks.
  * Removed `is1v1` gates from some late commodity buying rules.
  * Ten-minute pulse in constants now owns many late-game permissions.

* 60052_ai_wonder-kill.bin

  * Main Defend the Monument special-mode file retained.
  * Removed references to old `importantT4unique` and `importantT4heavy` goals.
  * Air Cruiser and Cannon counts now use generated TL4 constants.
  * Bounty Hunter response uses the age/alert-specific target constants; published warnings allow capped replenishment.
  * Added standardized header/comment structure.

* 60053_ai_wonder-rush.bin

  * Wonder Rush remains a large special-mode file.
  * Updated building references away from alias constants to real `BLDG-  *` names where touched.
  * Retains special economy, building, and attack behavior for wonder-rush mode.
  * Mirrors many prototype infrastructure, homebase, and production cleanup changes where copied into this mode.

* 60054_ai_resign.bin

  * Resign file has standardized headers and chapter labels.
  * Logic remains broadly aligned with the reference but documented/organized.

* 60055_ai_escrow.bin

  * Escrow file has standardized headers.
  * Removed old `importantT4unique` and `importantT4heavy` gates.
  * TL4 escrow behavior now keys off `importantT4research` instead.
  * Keeps age-based escrow percentages and release behavior.

* 60056_ai_military-population-hard.bin

  * Hard-difficulty military population constants were expanded into generated package thresholds.
  * Added p1/p2/p3/p4 package thresholds for staged unit production.
  * Added water, asteroid, and hybrid branch variants for many unit packages.
  * 250-pop Hard/Hardest land worker caps were raised to 96 with ally trade and 115 without ally trade.
  * Added detection-response constants for air, mech, Jedi, boats, and other support packages.
  * Added package constants for modern core-arm and support-unit selectors.

## Comparison Stats

```text
60001 age-advancement              658 ->    635  (-23)
60002 AGGRESSIVE                     67 ->     42  (-25)
60003 airbase                      591 ->   1587  (+996)
60004 animal                       164 ->    114  (-50)
60005 attack                      1571 ->   1747  (+176)
60006 building-count               376 ->    134  (-242)
60007 carbon                        51 ->    111  (+60)
60008 cheats                      1337 ->   3185  (+1848)
60009 civ-loads                     14 ->     27  (+13)
60010 combat-arm                   792 ->    862   (+70)
60011 constants                   1149 ->   1874  (+725)
60012 deathmatch                     8 ->     23  (+15)
60013 defensive                     51 ->    304  (+253)
60014 difficulty-loads              28 ->     41  (+13)
60015 dip-boomer                     2 ->     18  (+16)
60016 dip-bully                   1250 ->   1263  (+13)
60017 dip-feeder                   299 ->    313  (+14)
60018 diplomacy                    773 ->    661  (-112)
60019 fishboat                     394 ->    336  (-58)
60020 food                         160 ->    576  (+416)
60021 fortress                    1407 ->   3372  (+1965)
60022 ground                        46 ->     55  (+9)
60023 groups                         5 ->     22  (+17)
60024 heavy-weapons                406 ->   2099 (+1693)
60025 homebase                     785 ->    792  (+7)
60026 init-goals                    27 ->     38  (+11)
60027 jedi-temple                  359 ->    452   (+93)
60028 map-loads                   1141 ->   1165  (+24)
60029 map-specs                     34 ->     47  (+13)
60030 mech-factory                 416 ->   2042  (+1626)
60031 military-population           15 -> 423828  (+423813)
60032 monument                      27 ->     33  (+6)
60033 no-diplomacy                  35 ->     52  (+17)
60034 nova                         378 ->    265  (-113)
60035 ore                            1 ->    253  (+252)
60036 population                  2614 ->   2620  (+6)
60037 randomgame                   166 ->    187  (+21)
60038 research-center               25 ->    183  (+158)
60039 research                    2457 ->    748 (-1709)
60040 rush                           4 ->    111  (+107)
60041 shipyard                     583 ->   1549  (+966)
60042 sn-gather                    846 ->   1660  (+814)
60043 sn-homebase                 1098 ->   1109  (+11)
60044 sn-soldiers                  451 ->    485  (+34)
60045 spaceport                    688 ->    950  (+262)
60046 supplement                   291 ->    160  (-131)
60047 tower                        222 ->    342  (+120)
60048 troop-center                 832 ->   1989  (+1157)
60049 war-center                    53 ->    447  (+394)
60050 warboat-island              5673 ->   5646  (-27)
60051 warboat                      924 ->    224  (-700)
60052 wonder-kill                 1774 ->   1792  (+18)
60053 wonder-rush                 4048 ->   4022  (-26)
60054 resign                       680 ->    684  (+4)
60055 escrow                       169 ->    178  (+9)
60056 military-population-hard   73420 -> 423827  (+350407)
```
