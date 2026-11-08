# Initial attack strength check

Temporary playtest chat reports the first strength HOLD and first CLEAR per AI per match, with no further repetitions. CLEAR means this check released; other attack requirements still apply. Goal 224 tracks the two-message limit without using another timer.

Regular LAND games now check military population before launching ordinary TL3 and TL4 attacks or starting a Town Size Attack. This first version operates only when exactly one enemy remains in the game. Early raids, WATER, HYBRID, ASTEROID, Monument Race, and games with several remaining enemies retain their previous behavior. Separate Jedi attack commands and scripted emergency commands are outside this initial rollout.

The AI holds these launches when its military population falls below approximately 70% of the enemy's, then resumes once it reaches approximately 85%. The difference between the two thresholds prevents repeated switching. The comparison updates every script pass, so enemy losses can release a hold without waiting for more troops. Enemies with 20 or fewer military population bypass this initial check.

AoC cannot directly compare two changing population values. The rules place the enemy in a population band, then compare our population with fixed thresholds. Bands are 10 population wide through 100, 25 through 250, 50 through 500, and 100 through 1,000. Thresholds use the band's upper bound and round up. For an enemy with exactly 50 military population, we hold below 35 and release at 43; for 1,000, those thresholds are 700 and 850. Near the bottom of a band the check is more cautious than those percentages.

The rules use `player-in-game` and `players-stance` for slots 1–8 to establish a sole enemy. Only then do they sample `players-military-population any-enemy`. They change neither diplomacy nor engine targeting, and use no UP or DE commands. Goals 221–223 hold the state; goal IDs and strategic-number IDs are separate namespaces.

Military population includes unseen units and counts the entire military, including units already deployed or unable to reach the target. It does not estimate local combat strength. Existing production, defense, and Fortress siege requirements continue independently. The check does not recall an army already fighting or stop an already active Town Size Attack.

Validation covers reinforcement, enemy losses, hysteresis, all eight opponent slots, multiple/no opponents, early-age/map bypasses, the small-army boundary, 1,000-population thresholds, normal launches, Town Size Attack starts, and the independent Fortress hold. These are script-level checks; in-game behavior still needs playtesting.
