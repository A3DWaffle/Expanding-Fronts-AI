


60039_ai_research.bin
* Research file was reduced from broad tech handling to shared non-unit upgrades and important tech checks.
* Most unit-line techs were moved out to their unit production files.
* Important TL2 research is now personality-based.
* RUSH important TL2 research now focuses on early troop combat techs.
* DEFENSIVE now immediately clears important TL2 research.
* Important TL3 research is now personality-based.
* RUSH can clear important TL3 research once its TL2 troop techs are no longer available.
* Important TL4 research now also requires Optimized Motivator.
* Shield Modifications now prioritizes real air strategies and air unique units.
* Sensor Beacon and Sensor Array now require 3 Command Centers and important research timing.
* Defensive structure techs remain here but are gated later behind important research.

60040_ai_rush.bin
* Rush file is no longer empty/defunct.
* RUSH now sets openingstyle to RUSH if no personality was already assigned.
* RUSH can resume attacks in TL2 once it reaches 6 military population.
* RUSH pauses attacks in TL3 to recover and rebuild.
* RUSH resumes normal attacks again in TL4.

60041_ai_shipyard.bin
* First Shipyard now requires a Troop Center and Power Core.
* TL2 Shipyards now wait for Mech Factory, Spaceport, Power Core, and important TL2 research.
* TL3/4 Shipyards now wait for either 3 Command Centers or 2 Airbases.
* Fifth TL4 Shipyard now requires SEA strategy instead of specific boat civs.
* Boat upgrades no longer wait on important TL4 unique research.
* Fishing boat rules no longer stop just because the AI is close to population cap.
* TL2 naval army is now centered on Frigates, with AA Destroyers only added when enemy air is detected.
* TL3 naval production now requires SEA strategy and builds a staged Frigate, AA Destroyer, Destroyer, and Monitor package.
* TL4 naval production now requires SEA strategy and builds a staged Frigate, AA Destroyer, Destroyer, Cruiser, and Monitor package.
* Extra AA Destroyers now scale from enemy air detection in TL2/3/4.
* AT-AT Swimmer count now uses the water unique-unit constant.

60042_ai_sn-gather.bin
* Save-the-animals now starts when any herdables are found instead of waiting for 3+.
* RUSH and DEFENSIVE can build a late TL1 Animal Nursery if their opener missed one.
* TL1 gather rates now change by personality.
* RUSH now gathers nova in TL1 after building a Nova Proc Ctr.
* DEFENSIVE now gathers ore in TL1 after building an Ore Proc Ctr.
* Standard TL1 play now only gathers nova when stockpile is low.
* TL2 ore gathering is now synced across difficulties.
* TL2 hunt maps now keep more workers on food.
* RUSH TL2 now gathers more food/nova and less ore.
* DEFENSIVE TL2 now gathers more ore while building turrets, then shifts back toward food/nova.
* RUSH TL3 now uses a custom recovery gather setup while attacks are on hold.
* DEFENSIVE TL3 now uses a custom food/nova gather setup.

60043_ai_sn-homebase.bin
* Initial maximum food drop distance increased from 12 to 14.
* Initial maximum hunt distance increased from 30 to 40.
* Removed importantT4unique DONE checks from TL4 town-size expansion logic.
* TL4 town-size expansion now only waits on importantT4research DONE before trying to make room for missing buildings.

60044_ai_sn-soldiers.bin
* Projectile dodge behavior was disabled across difficulties by setting ability-to-dodge-missiles to 100.
* TL3/4 maintain-distance behavior was disabled by setting ability-to-maintain-distance to 100.
* RUSH and DEFENSIVE will use the first mounted unit to aid in scouting if an enemy Command Center has not been found.

60045_ai_spaceport.bin
* Spaceport techs moved back to this file.
* Confederacy Alliance, Piracy, and Cloaked Smuggling now require an ally before it can be researched.
* Commodity trading requires 3000+ stockpile before most trading rules activate.
* Routine metal buying was removed from small and medium trade rules.
* DEFENSIVE can sell ore for nova if food/carbon are ready but nova is blocking TL3.
* TL4 metal buying now requires much stronger spare nova/food/carbon stockpiles.
* Human tribute now requires the AI to have 3000+ of the requested resource before sending tribute.
* AI-to-AI tribute now requires 3000+ of the donated resource before sending food, carbon, nova, or ore.
* Spaceport-owned civ techs are handled in this file with escrow releases.

60046_ai_supplement.bin
* Removed SCN unit logic for now because it was using deparreciated constants.

60048_ai_troop-center.bin
* TL1 Troop Center now requires a power core, carbon ctr and a food proc ctr. It has a cap of 1 unless RUSH who will build another upon aging up.
* TL2 Troop Center requires a power core, mech factory, and spaceport. It has a cap of 2.
* TL3/4 Troop Center requires two airbases or two command centers. It has a cap of 2 if troopers play no part in the AI's strategy and 5 if they do.
* TL3/4 Trooper unit-line upgrades are only researched if AI strategy rolled TROOP or TROOP/HW. AA troopers are the exception.
* All Troop Center techs moved back to this file.
* All Troop Center techs updated so that the AI must be fielding units who can benefit from the techs before researching them.
* RUSH and DEFENSIVE will train TL1 mounties to apply pressure to opponent. This replaces the lone mounted unit attack. Once raiding is complete, they may train trooper recruits.
* AGGRESSIVE will periodically train trooper recruits for defense. Refrains from Mounted unit use in TL1.
* In TL2/3/4, Mounted units are trained when Laser Trooper quotas are met. 
* In TL3/4, If AI core strategy is not TROOP or TROOP/HW then it will stop training troopers except for AA troopers.
* In TL3/4, Grenade Troopers are trained when Laser Trooper quotas are met or if enemy is fielding too many mechs and Grenade Troopers are approved for use.
* In TL4, Laser Troopers are trained when either Artillery or Grenade Trooper quotas are met.

60049_ai_war-center.bin
* Logic for War Center research moved back here.
* The AI will only make a War Center in TL2 if it is RUSH personality.
* TL3 War Centers require either 2 airbases or 2 command centers.
* The AI will build a max of two.
* All War Center techs updated so that the AI must be fielding units who can benefit from the techs before researching them.
* All War Center techs moved to TL3 and later unless it is the RUSH personality.

60050_warboat-island.bin
* Restored and cleaned dialogue behavior.

60047_ai_tower.bin
* Tower file now controls defensive walls, turret behavior, and cleanup in one place.
* Walls are disabled by default instead of being broadly available.

60038_ai_research-center.bin
* Research Center tech handling moved into this file.
* First Research Center now requires TL3 and 3 Command Centers.
* Second Research Center remains a TL4 follow-up and caps the AI at 2.
* Added Research Center core tech rules.
* Added Research Center unique tech rules.
* Tracking and Targeting Computers now waits for important TL3 research.
* TL4 economy/building techs now wait for important TL4 research.
* Defensive Research Center techs can be researched early by DEFENSIVE, or later by other personalities after important TL4 research.

60037_ai_randomgame.bin
* Added `military-population` to the always-loaded constants so lower difficulty package sizes are available.
* Added `combat-arm` to normal random-map setup so personality and army package rolls happen before production files load.
* Added random personality overlay loading for AGGRESSIVE, DEFENSIVE, and RUSH.
* Normal mode load order now supports the new split between core strategy, economy, research, and unit production files.
* Monument Race and Defend the Monument load paths were updated to the new format.

60035_ai_ore.bin
* Ore file is no longer empty.
* Ore processing logic was moved back into this file from nova.
* DEFENSIVE now builds an Ore Proc Ctr in TL1 as part of its opening.
* DEFENSIVE can force an Ore Proc Ctr in TL2 once its basic economy is online.
* Ore mining techs now wait on important research timing.
* Added fallback handling for maps where ore is too far away or runs out.

60034_ai_nova.bin
* Nova file now only handles nova processing and nova mining techs.
* Ore processing logic was moved out to the ore file.
* TL1/TL2 Nova Proc Ctr construction now requires carbon infrastructure and a Troop Center, and caps at 1 early proc.
* Nova mining techs now wait on important research timing.

60031_ai_military-population.bin
* Military population constants were expanded into generated package thresholds.
* Added `snc-pop-limit` setup for each population cap.
* Added p1/p2/p3/p4 package thresholds for staged unit production.
* Added water-map variants for many unit packages.
* Added detection-response constants for air, mech, Jedi, and other support packages.
* Added package constants for modern core-arm and support-unit selectors.
* Added worker, cargo, fishing boat, and population pressure constants used by economy and production files.

60030_ai_mech-factory.bin
* Mech Factory now handles building, mech upgrades, and mech production packages in one file.
* TL2 Mech Factory requires a Power Core.
* TL3 Mech Factory construction is paced behind economy/building progress.
* TL4 Mech Factory count scales higher when MECH, MECH/HW, Assault Mech support, or support-assault-mech is active.
* Mech upgrades moved back into this file.
* TL3 Strike Mechs can be trained as a defensive/trickle response.
* TL3 Mech Destroyers are tied to MECH strategy and mech detection pressure.
* TL4 Mech production is staged by p1/p2/p3/p4 package thresholds.
* Transport Mechs are treated as support tied to troop-style packages rather than generic mech spam.

60027_ai_jedi-temple.bin
* Jedi Temple now handles temple construction, Jedi units, Jedi Masters, temple unique units, and temple techs.
* Standard Jedi Temple is delayed until TL3 with Troop Center, Mech Factory, Spaceport, and 3 Command Centers online.
* Black Sun can build an earlier temple through its special path.
* Holocron collection now trains a Jedi or Black Sun hunter and retries for a limited time.
* Holocron collection gives up after long game time instead of trying forever.
* Jedi Masters now require Master support and sufficient military population before spending nova.
* Temple unique units now use combat-supp and support flags.
* Jedi and temple techs now wait on relevant unit presence and important research timing.

60025_ai_homebase.bin
* Homebase now owns core base infrastructure: Command Centers, workers, prefabs, farms, power cores, and medics.
* Command Center expansion now scales through TL3/TL4 constants and late-game TSA pressure.
* Worker production now uses modern worker caps, water-map worker caps, and late-game worker trimming.
* Prefab Shelter logic now builds earlier and keeps larger housing headroom in TL2+.
* Farm logic now handles TL1 emergency food, berry/no-berry cases, hunt-map transitions, and TL2+ farm support.
* Power Core construction now supports TL1 spine building and larger TL2/TL4 power needs.

60024_ai_heavy-weapons.bin
* Heavy Weapons Factory now handles building, siege upgrades, and siege production packages in one file.
* TL3 Heavy Weapons Factory construction is tied to artillery/HW strategy or support artillery needs.
* TL4 Heavy Weapons Factory count scales higher for TROOP/HW, MECH/HW, ARTILLERY support, or support-artillery.
* Artillery upgrades moved back into this file and now wait for artillery/HW strategy or support.
* Pummel upgrades wait on important TL4 research.
* TL3 missile and artillery production use staged p1/p2/p3 thresholds.
* TL3 Rams can be added once important TL3 research is complete.
* TL4 Rams are available for MECH strategy to help AI break obstacles without friendly-fire.
* TL4 artillery and ram support use water-map constants where applicable.

60021_ai_fortress.bin
* Air Cruiser production is tied to AIR strategy or Aircraft support.
* Cannon production now follows modern combat-arm/support logic instead of old 1v1-specific caps.
* TROOP and TROOP/HW can use more Cannons as late siege.
* Fortress techs now wait on important TL4 research where appropriate.
* Fortress unique unit techs were moved back into this file.

60020_ai_food.bin
* Initial Food Proc Ctr timing now distinguishes berries, no-berries, and hunt maps.
* Hunt maps delay the first food proc briefly so early workers can use nearby hunt.
* Added a TL1 hunt-food phase before deciding on extra food dropoffs.
* TL2 hunt maps use tighter dropoff behavior to reduce overextension.
* Food Proc Ctr expansion is capped more carefully in TL1.
* Later Food Proc Ctr expansion uses distance and resource-state checks.

60013_ai_defensive.bin
* Defensive file now sets openingstyle to DEFENSIVE if no personality was assigned.
* DEFENSIVE keeps TL2 attacks on hold.
* DEFENSIVE starts fighter trick behavior in TL3.
* DEFENSIVE can release attack holds after building enough military population.
* DEFENSIVE uses higher attack thresholds than RUSH or AGGRESSIVE.

60011_ai_constants.bin
* Added modern combat-arm and support package constants.
* Added modern air and mech alert ladder constants.
* Added `enemymechsighted` and `snc-enemy-mech-detection` support.
* Added support flags for the expanded support-unit selector.
* Removed many deprecated alternate building-name dependencies from active logic.
* Mech unique detection uses valid mech/anti-mech unit names and excludes invalid old entries.

60010_ai_combat-arm.bin
* Added the modern core combat-arm and support package selector.
* AI now rolls a core army plan from civ-specific matrices.
* Support package flags can layer multiple support roles on top of the older single support enum.
* WATER no longer forces combat-arm SEA, so river/lake maps can still roll land, air, or mech strategies.
* SEA remains available as a legacy package label but is no longer the default water-map army plan.

60008_ai_cheats.bin
* Cheats file now handles difficulty resource support, refunds, and build-order recovery.
* AI cheat timer cadence was adjusted for the new opener/package logic.
* Early worker food support remains for Moderate+ so worker production does not stall.
* Refund goals are used for proc centers, power cores, and other early infrastructure.
* Cheat behavior is more targeted around build-order failures and resource shortfalls instead of broad constant income.

60007_ai_carbon.bin
* Carbon file now handles Carbon Proc Ctrs and carbon-side economy techs.
* First Carbon Proc Ctr waits for initial food infrastructure and avoids interrupting animal-saving behavior.
* Added timeout fallback if the AI still has no Carbon Proc Ctr.
* TL2+ Carbon Proc Ctr expansion uses distance checks and escrow.
* Carbon-side economy techs are handled from this file.

60006_ai_building-count.bin
* Building-count now focuses on builder assignment and building-count milestones.
* TL1 uses one builder per key structure to avoid early worker overcommit.
* TL2+ restores larger builder counts for faster construction.
* Older strategic building-count behavior has been largely deprecated.

60005_ai_attack.bin
* Attack file now handles personality attack pacing, attack holds, TSA, AIRWAVE, and special attack cases.
* Personality announcement and attack posture now follow the selected openingstyle.
* Important research goals can hold attacks until the AI is ready.
* TL1 attacks no longer launch with only Trooper Recruits.
* RUSH and DEFENSIVE TL1 pressure uses Mounted Troopers instead.
* TL2 RUSH attacks now require 10 military population.
* TL2 RUSH wave count is randomly capped at 1 or 2 attacks.
* TL2 attack rules use longer pacing instead of rapid 90-second pressure.
* TL2 timer-triggered attack branches now avoid stacking multiple attack-ready states in the same timer window.
* TL2 AI ally join-in attacks are blocked to avoid attack-command loops.
* Aggressive and Defensive TL2 now use the shared TL2 launcher instead of bypassing cooldown logic.
* TSA can start when military population gets too large and can exit again when population drops.
* Max-pop attacks and TSA behavior were simplified around modern population thresholds.

60004_ai_animal.bin
* Animal techs were moved back into this file.
* Acklay support is tied to the modern support selector.
* Nexu are only trained by RUSH in TL3.
* Reeks are only trained by RUSH after Acklay quota is met.
* Probots and Vornskyrs removed from AI lineup, accomplishes nothing.

60003_ai_airbase.bin
* DEFENSIVE can prioritize earlier TL3 Airbases.
* Non-DEFENSIVE Airbases wait for stronger economy/building progress.
* Airbase count scales higher for AIR strategy, aircraft support, or bomber support.
* Aircraft upgrades now check that the AI is using relevant aircraft packages.
* Bombers use mech detection pressure for staged support production.
* Fighter production remains the default air response when bombers are not justified.
* In TL4, Attackers become core air force. Interceptors, Fighters and Bombers are unlocked in that order when Attacker quota is met.

60002_ai_agressive.bin
* Aggressive file now sets openingstyle to AGGRESSIVE if no personality was assigned.
* AGGRESSIVE can release attack holds from TL2 onward once it has a small military force.
* AGGRESSIVE uses lower attack thresholds than DEFENSIVE and higher pacing than RUSH.
