# Changelog

## 2026-11-05 - Expanding Fronts AI update

### Attacks and scouting

- **Fortresses change when the AI attacks.** After spotting an enemy Fortress in a regular match, the AI holds new attacks in Tech Levels 3 and 4 until it has enough siege. In TL3 it needs Artillery. In TL4 either Artillery or Cannons can meet the requirement on their own. The required number comes from the map's second production target (P2). Only completed units count, and the AI remembers the Fortress after losing sight of it. The hold also applies to Jedi-led attacks and Town Size Attacks.
- **TL1 raiders can pull back under pressure.** If the AI has registered an incoming attack and has no recent sighting of enemy workers, it calls for a retreat and holds new raids. It remembers the attack for roughly 25–30 game seconds and worker sightings for roughly 10–15. A raid that loses its troops clears after two consecutive checks, and a recall can time out after about a minute so the AI can try again.
- **Aggressive and Defensive have distinct TL2 plans.** Aggressive can launch its own attack after the game has reported it under attack, provided it meets its normal launch requirements. Defensive holds TL2 attacks and skips new scout assignments while it focuses on its base. The AI also holds new scouts during active raids and when it has recently registered an incoming attack.

### Base defense and mines

- **Defensive prioritizes three Laser Turrets in TL2.** It requests eight builders for the opening turrets before opening most production and tech construction. Power, housing, and essential resource drop-offs can still go up. After the third turret, the builder assignment drops to five, the same target the other personalities use from TL2 onward.
- An attack can pause affected construction for 30 game seconds. The pause runs its full duration through brief breaks in the attack signal. Construction can resume when the pause expires.
- **The AI can build mines in TL2.** It needs a completed Carbon Processing Center, Nova Processing Center, or Laser Turret, plus more than 300 spendable carbon. It stops placing new orders when it has five live mines of its own.

### Air and naval balance

- **Interceptors are now a response to enemy air.** In regular matches, TL4 aircraft-support lineups train them only while a Low, Guard, or Danger air alert is active.
- **Hybrid fleets get three more boats per enabled production target.** This applies to fishing boats and warships across population settings and difficulties. At 250 population, the Hybrid AA Destroyer target rises from four to seven.

### Housing, ore, and Cannons

- **Prefab Shelter limits scale with the match population cap.** The AI builds as housing runs low and counts shelters already under construction. With one Command Center and no other housing sources, the shelter ceilings are 4 at 25 population, 49 at 250, and 199 at 1,000. Regular matches no longer grant free housing when the AI reaches 200 population.
- **The AI relies more on ore mining.** Positive scripted ore grants and reimbursements are now one quarter of their previous amounts, rounded down to a minimum of one. The recurring top-up below 30 ore is gone. Any personality can build its first Ore Processing Center from TL2 once ore is found, metal is below 150, carbon exceeds 200, and a Carbon Processing Center, Troop Center, and Power Core are complete.
- **Cannons come out in smaller numbers and at a slower pace.** Positive production targets were halved and rounded up. Cannon orders share a cooldown of about 60–65 game seconds across all Fortresses. The late-game fallback fills a one-Cannon target using spendable resources and gives Bounty Hunters priority.
- The AI now recognizes live Lava Fleas as a hunting opportunity. During the TL1-to-TL2 transition, it can train toward its first TL2 Trooper target. Defensive has a one-time 50% chance to choose a mounted opening.

### Game modes and fixes

- **Monument Race:** Removed duplicated sections of the AI script and restored the intended TL2 advancement rule. Each difficulty now runs a single copy of its timed income rules. Prefab Shelter construction also follows the match population cap.
- **Defend the Monument:** The affected Fortress construction rules now stop at three, replacing limits that ranged from four to ten.
- Removed public debug messages about the AI's opening, army composition, support units, and attack routing. Players still receive treaty notices, scenario dialogue, and resignation messages.

## 2026-08-31 - Computer Prototype Modernization Pass

This changelog summarizes the current `Computer Prototype` AI pass. Detailed file-by-file notes remain in `PATCH_NOTES_DRAFT.md`.

### Economy

* Reworked TL1 food and carbon opening behavior so the AI builds a real Food Proc Ctr + Carbon Proc Ctr economy before aging.
* Hunt openings now delay the first Food Proc Ctr briefly, prefer local hunt, and avoid chasing edge-map animals.
* Only verified food-lure animals now enable the hunt economy path, preventing non-food lure classes from breaking no-berry starts.
* Boar/lure task groups are smaller and more local:
  * `sn-maximum-hunt-drop-distance` is now `30`.
  * `sn-minimum-boar-hunt-group-size` starts at `99` to block opening lure parties, then relaxes to `3` after 4 minutes.
* No-berry hunt starts can now add the first safety farm after 4 minutes instead of waiting 10 minutes.
* TL1/TL2 emergency farm support now reacts to food collapse and carbon overflow.
* TL2 builder assignments are calmer:
  * Mech Factory and Spaceport use `2` builders.
  * Farms use `2` builders.
  * Most secondary buildings and turrets use `1` builder.
* TL2 economy now prioritizes the Mech Factory + Spaceport spine while keeping nova active.
* TL2 ore gathering is limited to a small top-up role and shuts off once stockpile is healthy.
* TL2-to-TL3 age-up now pivots to `30/40/30` carbon/food/nova and cuts ore to `0`.
* TL3/TL4 food-collapse recovery rebuilds farms and forces stronger food gathering when the economy stalls.
* Late farm and Food Proc Ctr caps were raised so the AI can sustain larger armies.
* TL4 Power Core overbuild was reduced, and rich forward-base support is more selective.

### Teching And Research

* Easy/Easiest no longer automatically force age-match behavior.
* TL2 age-up requires 10+ workers plus Food Proc Ctr and Carbon Proc Ctr.
* TL3 age-up waits at least 120 seconds in TL2.
* TL4 age-up waits for farm infrastructure, with the hard timed fallback moved from 28 minutes to 25 minutes.
* Research handling was split back into the production files that use those upgrades.
* Important TL2/TL3/TL4 research goals now guide attack timing and expensive tech spending.
* Temple tech coverage was restored:
  * Faith in the Force and Force Purge receive priority gates.
  * Secondary Force upgrades wait until Jedi Masters are actually being used.
* Basic food, carbon, nova, and ore economy techs can start during the age-up to the next tech level.

### Buildings

* First TL1 Troop Center requires Power Core, Food Proc Ctr, and Carbon Proc Ctr.
* First TL2 Mech Factory and Spaceport are treated as the TL2 spine.
* Secondary TL2 buildings wait behind the Mech Factory + Spaceport spine where appropriate.
* TL2 Troop Center expansion requires the TL2 spine, except Rush can follow its pressure path.
* War Center, Jedi Temple, Heavy Weapons Factory, Shipyard, and other production buildings have tighter strategy gates.
* Forward Food Proc Ctr placement was disabled after testing showed it could place near enemy bases.
* Rich TL4 forward production and defense buildings now have stricter caps and stockpile checks.

### Combat And Attacks

* Added modern personality flow for `AGGRESSIVE`, `DEFENSIVE`, and `RUSH`.
* Added modern `combat-arm` selection with support flags for aircraft, sea, artillery, mounted, masters, unique units, and other support roles.
* Water, hybrid, and asteroid maps now influence support packages more cleanly.
* TL1/TL2 attacks can target opening economy buildings, heavily favoring Carbon Proc Ctrs.
* TL1/TL2 attacks switch back to worker targeting after launch.
* TL3+ uses worker targeting and does not participate in the opening building-target experiment.
* TL1 attacks no longer launch with only Trooper Recruits.
* RUSH and DEFENSIVE use Mounted Troopers for TL1 pressure.
* TL1 recruits stay cheap at p1 unless the AI is already aging up.
* TL2 Rush pressure uses paced wave counts and longer attack cooldowns.
* Defensive TL2 attacks stay on hold while the AI stabilizes.
* Sentry-distance clamps were added to reduce unit spread:
  * TL2 max sentry distance `14`.
  * TL3 max sentry distance `16`.
  * TL4 max sentry distance `18`.

### Unit Production

* Military population tables were regenerated with staged p1/p2/p3/p4 package thresholds.
* Normal population caps now scale from the hard tables at roughly half value.
* Hard/Hardest 250-pop worker caps were raised so late-game economies can support bigger farm plans.
* Air, mech, troop, heavy-weapons, naval, Jedi, unique-unit, and detection-response packages were modernized.
* TL3/TL4 Fighter cover no longer waits on Attacker quotas before continuing production.
* Bombers are delayed behind stronger Attacker progress so nova is not spent too early.
* AA Mobile and AA Trooper response thresholds were made easier to reach without overcommitting.
* Pummel/Ram production remains disabled to avoid wasteful spending.
* Transport Mechs are treated as support for troop-style packages instead of generic mech spam.
* Zann can now research Grenadier Training without requiring a Grenadier support package.
* Assault Mechs return to normal TL4 MECH and MECH/HW production, with all Assault Mech rules unlocked from p2 package progress instead of late-stage artillery or mech quotas.

### Diplomacy, Trade, And Cheats

* Difficulty income was retuned:
  * Moderate stays conservative.
  * Hard gets stronger contest support.
  * Hardest gets a higher sustained-income ceiling.
* Routine TL1 carbon cheat income was removed; early support now comes from targeted refunds and stuck-age help.
* Hard/Hardest routine TL2 nova and carbon support were reduced while severe catch-up support remains.
* Commodity trading requires much larger stockpiles before routine use.
* Routine ore buying was reduced.
* Defensive can sell ore for nova when nova blocks TL3.
* AI tribute rules now require large stockpiles before donating resources.

### Cleanup

* The AI was reorganized into a modular prototype load chain using explicit `/Computer Prototype/...` loads.
* Many files now have standardized headers, chapter labels, and clearer ownership.
* Deprecated building aliases were removed from active rules; touched logic now uses real `BLDG-*` names.
* Large obsolete or defunct behavior blocks were reduced or moved to the files that own the behavior.
* Parser-sensitive rules were split into smaller, safer rules where needed.
