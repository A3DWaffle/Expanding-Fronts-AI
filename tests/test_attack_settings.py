"""Run with: python -m unittest discover -s tests -v (standard library only)."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
COMMITMENTS = {'sn-percent-attack-soldiers', 'sn-percent-attack-air', 'sn-percent-attack-boats'}


def forms(text):
    tokens = re.findall(r';[^\n]*|"(?:\\.|[^"\\])*"|\(|\)|[^\s();]+', text)
    stack, result = [], []
    for token in tokens:
        if token.startswith(';'):
            continue
        if token == '(':
            stack.append([])
        elif token == ')':
            node = stack.pop()
            (stack[-1] if stack else result).append(node)
        elif stack:
            stack[-1].append(token)
    assert not stack
    return result


class SettingsState:
    def __init__(self, profile='AGGRESSIVE', mode='LAND', age=3, spare=8, ready=True, kind='NORM'):
        self.goals = {'openingstyle': 'STYLE-' + profile, 'special-map': mode,
                      'aready': 'YES' if ready else 'NO', 'attacktype': kind,
                      'ground-release-state': 'GROUND-READY' if spare >= 8 else 'GROUND-GATHERING'}
        self.age, self.spare = age, spare
        self.sn = dict.fromkeys(COMMITMENTS, 37)
        self.actions = []

    def value(self, token):
        return {'tech-level-3': 3, 'land-wave-rush': 8}.get(
            token, int(token) if re.fullmatch(r'-?\d+', token) else token)

    def fact(self, node):
        op, *args = node
        if op == 'true':
            return True
        if op == 'goal':
            return self.goals.get(args[0]) == args[1]
        if op == 'not':
            return not self.fact(args[0])
        if op in ('and', 'or'):
            return (all if op == 'and' else any)(self.fact(n) for n in args)
        if op == 'current-age':
            left, comparator, right = self.age, args[0], self.value(args[1])
        elif op == 'defend-soldier-count':
            left, comparator, right = self.spare, args[0], self.value(args[1])
        else:
            raise AssertionError('Unexpected setting fact: ' + str(node))
        return {'>=': left >= right, '<': left < right}[comparator]

    def run(self):
        for rule in forms((ROOT / 'groups.per').read_text()):
            self.assert_rule(rule)
            split = rule.index('=>')
            if all(self.fact(n) for n in rule[1:split]):
                for action in rule[split + 1:]:
                    self.actions.append(action)
                    self.sn[action[1]] = self.value(action[2])

    @staticmethod
    def assert_rule(rule):
        assert rule[0] == 'defrule'
        for action in rule[rule.index('=>') + 1:]:
            assert action[0] == 'set-strategic-number' and action[1] in COMMITMENTS


class AttackSettingsTests(unittest.TestCase):
    def test_personality_commitments_across_maps(self):
        for profile, percent in [('RUSH', 100), ('AGGRESSIVE', 75), ('DEFENSIVE', 50)]:
            for mode in ('LAND', 'HYBRID', 'WATER', 'ASTEROID'):
                for spare in (0, 7, 8, 30):
                    s = SettingsState(profile=profile, mode=mode, spare=spare)
                    s.run()
                    ground = (100 if spare >= 8 else 0) if mode == 'WATER' else percent
                    boats = 100 if mode in ('WATER', 'HYBRID') else percent
                    self.assertEqual(s.sn, {'sn-percent-attack-soldiers': ground,
                                           'sn-percent-attack-air': percent,
                                           'sn-percent-attack-boats': boats})

    def test_no_repeated_commitment_after_launch_consumes_readiness(self):
        s = SettingsState(mode='WATER', spare=7)
        s.run()
        s.goals['aready'] = 'NO'
        s.actions = []
        s.run()
        self.assertEqual(s.actions, [])

    def test_early_age_and_tsa_keep_their_existing_behavior(self):
        s = SettingsState(mode='WATER', age=2, spare=0)
        s.run()
        self.assertEqual(set(s.sn.values()), {75})
        for spare in (0, 8):
            s = SettingsState(mode='WATER', spare=spare, kind='TSA')
            s.run()
            self.assertEqual(s.sn['sn-percent-attack-soldiers'], 100 if spare >= 8 else 0)
            self.assertEqual(s.sn['sn-percent-attack-air'], 37)
            self.assertEqual(s.sn['sn-percent-attack-boats'], 37)

    def test_groups_is_the_only_ready_attack_commitment_owner(self):
        owners = []
        for path in ROOT.glob('*.per'):
            if path.name in ('wonder-kill.per', 'wonder-rush.per'):
                continue  # Separate special-mode controllers are explicit exceptions.
            for rule in forms(path.read_text()):
                if rule[0] != 'defrule' or ['goal', 'aready', 'YES'] not in rule:
                    continue
                if any(isinstance(n, list) and n[0] == 'set-strategic-number'
                       and n[1] in COMMITMENTS for n in rule):
                    owners.append(path.name)
        self.assertEqual(owners, ['groups.per'] * 6)

    def test_include_is_immediately_before_ordinary_execution(self):
        attack = forms((ROOT / 'attack.per').read_text())
        include = ['load', '"/Computer Prototype/groups"']
        self.assertEqual(attack.count(include), 1)
        next_rule = attack[attack.index(include) + 1]
        self.assertIn(['goal', 'attacktype', 'NORM'], next_rule)
        self.assertIn(['current-age', '==', 'tech-level-1'], next_rule)
        self.assertIn(['attack-now'], next_rule)

    def test_settings_module_stays_within_engine_rule_budget(self):
        def nodes(node):
            return 1 + sum(nodes(n) for n in node[1:] if isinstance(n, list))
        for rule in forms((ROOT / 'groups.per').read_text()):
            SettingsState.assert_rule(rule)
            self.assertLessEqual(sum(nodes(n) for n in rule[1:] if isinstance(n, list)), 16)


if __name__ == '__main__':
    unittest.main()
