"""Shared ground decision tests; no engine movement or loading simulation."""
import unittest
from test_attack_settings import ROOT, SettingsState, forms


class GroundState(SettingsState):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.goals.update({'land-attack-policy': 'NO', 'land-core-ready': 'YES',
                           'land-regroup-phase': '0', 'fortress-siege-hold': 'NO',
                           'attack-strength-hold': 'NO', 'raid-launch-open': 'YES'})

    def value(self, token):
        return {'land-wave-rush': 8, 'land-wave-aggressive': 11,
                'land-wave-defensive': 16}.get(token, super().value(token))

    def decide(self):
        for rule in forms((ROOT / 'ground.per').read_text()):
            split = rule.index('=>')
            if all(self.fact(n) for n in rule[1:split]):
                for action in rule[split + 1:]:
                    assert action[0] == 'set-goal'
                    self.goals[action[1]] = self.value(action[2])
        return self.goals['ground-release-state']


class GroundReadinessTests(unittest.TestCase):
    def test_shared_personality_and_water_thresholds(self):
        for mode in ('LAND', 'HYBRID', 'WATER'):
            for profile, threshold in [('RUSH', 8), ('AGGRESSIVE', 11), ('DEFENSIVE', 16)]:
                threshold = 8 if mode == 'WATER' else threshold
                for age in (3, 4):
                    s = GroundState(mode=mode, profile=profile, age=age, spare=threshold - 1)
                    self.assertEqual(s.decide(), 'GROUND-GATHERING')
                    self.assertEqual(s.goals['ground-pulse-open'], 'NO')
                    s.spare = threshold
                    self.assertEqual(s.decide(), 'GROUND-READY')
                    self.assertEqual(s.goals['ground-pulse-open'], 'YES')

    def test_core_holds_and_rebuilding_override_an_available_batch(self):
        for flag, value, expected in [
            ('fortress-siege-hold', 'YES', 'GROUND-HELD'),
            ('attack-strength-hold', 'YES', 'GROUND-HELD'),
            ('land-regroup-phase', '2', 'GROUND-REBUILDING'),
            ('land-core-ready', 'NO', 'GROUND-CORE-LOW'),
        ]:
            s = GroundState(spare=40)
            s.goals.update({'land-attack-policy': 'YES', flag: value})
            self.assertEqual(s.decide(), expected)
            self.assertEqual(s.goals['ground-pulse-open'], 'NO')
            s.goals[flag] = 'YES' if flag == 'land-core-ready' else ('0' if flag == 'land-regroup-phase' else 'NO')
            self.assertEqual(s.decide(), 'GROUND-READY')

    def test_water_hold_changes_ground_only(self):
        s = GroundState(mode='WATER', spare=0)
        s.decide()
        s.run()
        self.assertEqual(s.sn['sn-percent-attack-soldiers'], 0)
        self.assertEqual(s.sn['sn-percent-attack-boats'], 100)
        self.assertEqual(s.sn['sn-percent-attack-air'], 75)

    def test_permission_is_recomputed_and_does_not_override_raid_hold(self):
        s = GroundState(spare=40)
        self.assertEqual(s.decide(), 'GROUND-READY')
        s.goals['raid-launch-open'] = 'NO'
        self.assertEqual(s.decide(), 'GROUND-READY')
        self.assertEqual(s.goals['ground-pulse-open'], 'NO')
        s.spare = 0
        self.assertEqual(s.decide(), 'GROUND-GATHERING')

    def test_both_master_launches_consume_the_shared_permission(self):
        pulses = [r for r in forms((ROOT / 'attack.per').read_text()) if
                  ['attack-now'] in r and any(['goal', 'jediattack', phase] in r
                  for phase in ('JEDIATTACK-READY', 'JEDIATTACK-RETRY'))]
        self.assertEqual(len(pulses), 2)
        for rule in pulses:
            self.assertIn(['goal', 'ground-pulse-open', 'YES'], rule)
            self.assertIn(['set-goal', 'ground-release-state', 'GROUND-COMMITTED'], rule)
            self.assertIn(['set-goal', 'ground-pulse-open', 'NO'], rule)

    def test_readiness_include_precedes_master_launches(self):
        attack = forms((ROOT / 'attack.per').read_text())
        include = ['load', '"/Computer Prototype/ground"']
        self.assertEqual(attack.count(include), 1)
        for index, rule in enumerate(attack):
            if ['goal', 'ground-pulse-open', 'YES'] in rule:
                self.assertLess(attack.index(include), index)

    def test_early_raids_air_sea_and_asteroid_keep_their_policy_scope(self):
        for mode, age, arm in [('LAND', 2, 'TROOP'), ('ASTEROID', 4, 'TROOP'),
                               ('LAND', 4, 'AIR'), ('HYBRID', 4, 'SEA')]:
            s = GroundState(mode=mode, age=age, spare=0)
            s.goals['combat-arm'] = arm
            self.assertEqual(s.decide(), 'GROUND-BYPASS')
            self.assertEqual(s.goals['ground-pulse-open'], 'YES')


if __name__ == '__main__':
    unittest.main()
