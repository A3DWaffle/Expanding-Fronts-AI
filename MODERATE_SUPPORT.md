# Moderate support reduction — November 7, 2026

For ordinary matches, Moderate's automatic scripted resource support is now limited to these one-time packets, paid after spending more than 20 game seconds in the reached Tech Level:

| Reached level | Carbon | Food | Nova | Ore |
|---|---:|---:|---:|---:|
| TL2 | 100 | 100 | 0 | 0 |
| TL3 | 150 | 150 | 75 | 0 |
| TL4 | 200 | 200 | 100 | 0 |

Each packet disables itself after paying. These are resource grants after advancement, not free age research. There is no worker-count multiplier or recurring income packet. A normal TL1 start receives no automatic grant until reaching TL2.

The Command Center line-of-sight fix (`aic-cc-los`) remains available after 120 game seconds. Moderate already excluded the regular AI trade boosts, garrison combat boosts, RMS training-speed boost, and free population technology.

Removed automatic support:

- The initial 2-food adjustment and repeating 5-food TL1 worker support.
- The one-time 40-carbon late Troop Center subsidy.
- Shipyard refunds of 45 carbon; TL2+ Power Core refunds of 60 carbon.
- Carbon Proc Ctr refunds of 20 carbon in TL1 or 40 later; Food/Nova Proc Ctr refunds of 50 of the respective resource; Ore Proc Ctr refunds of 12 ore.
- Reimbursements of 15 ore for each of the first four Laser Turrets.

Other difficulties' active cheat rules are unchanged. Explicitly requested configuration cheats, including Extreme/Turbo overrides and manual resource taunts, remain available; those are outside the default Moderate policy. Monument Race and Defend the Monument retain their separate scenario support.

## Destroyer verification

Existing TL3/TL4 WATER/HYBRID rules already raise Destroyer production in response to enemy combat-boat sightings. Alert levels trigger at 1, 6, 11, and 21 units in any one of five combat-boat families: Frigates, Destroyers, Cruisers, AA Destroyers, and Monitors. Fishing and transport boats do not trigger these alerts. Mixed families are checked separately rather than summed. Sighting levels feed the existing 300-game-second memory cycle.

The first alert fills the normal P2 Destroyer target. Higher alerts use larger, increasing response targets above normal P2. Production still requires resources, population room, and an available Shipyard. Sixteen response rules cover both ages, both map modes, and all four alert levels. This update verifies those existing rules without changing naval production.
