from dataclasses import dataclass
from copy import deepcopy
from collections import deque


@dataclass
class Spell:
    name: str
    cost: int
    damage: int = 0
    healing: int = 0
    armor: int = 0
    duration: int = 0
    mana: int = 0


class Player:
    def __init__(self, hitpoints, mana):
        self.hitpoints = hitpoints
        self.mana = mana
        self.armor = 0
        self.effects = {}
        self.mana_spent = 0

    def apply_effects(self):
        expired_effects = []
        for effect in self.effects:
            if effect == "Shield":
                self.armor = 7
            elif effect == "Recharge":
                self.mana += 101
            self.effects[effect] -= 1
            if self.effects[effect] == 0:
                expired_effects.append(effect)
        for effect in expired_effects:
            if effect == "Shield":
                self.armor = 0
            del self.effects[effect]

    def cast_spell(self, spell):
        if spell.cost > self.mana:
            return False
        self.mana -= spell.cost
        self.mana_spent += spell.cost
        if spell.duration > 0:
            if spell.name in self.effects:
                return False
            self.effects[spell.name] = spell.duration
        else:
            if spell.name == "Magic Missile":
                return spell.damage, 0
            if spell.name == "Drain":
                return spell.damage, spell.healing
        return 0, 0


class Boss:
    def __init__(self, hitpoints, damage):
        self.hitpoints = hitpoints
        self.damage = damage


def apply_poison(boss, effects):
    if "Poison" in effects:
        boss.hitpoints -= 3
        effects["Poison"] -= 1
        if effects["Poison"] == 0:
            del effects["Poison"]


def simulate_game(player, boss, spell_sequence):
    player = deepcopy(player)
    boss = deepcopy(boss)
    for spell in spell_sequence:
        # Player's turn
        player.apply_effects()
        apply_poison(boss, player.effects)

        if boss.hitpoints <= 0:
            return player.mana_spent

        if spell.cost > player.mana or (spell.name in player.effects and player.effects[spell.name] > 0):
            return float('inf')
        damage, healing = player.cast_spell(spell)
        boss.hitpoints -= damage
        player.hitpoints += healing

        if boss.hitpoints <= 0:
            return player.mana_spent

        # Boss's turn
        player.apply_effects()
        apply_poison(boss, player.effects)

        if boss.hitpoints <= 0:
            return player.mana_spent

        damage = max(1, boss.damage - player.armor)
        player.hitpoints -= damage

        if player.hitpoints <= 0:
            return float('inf')

    return float('inf')


def find_least_mana_sequence(player, boss, spells):
    best_mana_cost = float('inf')
    best_sequence = []

    queue = deque([(0, [], deepcopy(player), deepcopy(boss))])
    while queue:
        current_mana_spent, spell_sequence, player_state, boss_state = queue.popleft()

        if current_mana_spent >= best_mana_cost:
            continue

        for spell in spells:
            new_player = deepcopy(player_state)
            new_boss = deepcopy(boss_state)
            new_sequence = spell_sequence + [spell]
            mana_cost = simulate_game(new_player, new_boss, new_sequence)

            if mana_cost < best_mana_cost:
                best_mana_cost = mana_cost
                best_sequence = new_sequence

            if new_boss.hitpoints > 0 and new_player.hitpoints > 0:
                queue.append((current_mana_spent + spell.cost, new_sequence, new_player, new_boss))

    return best_mana_cost, best_sequence


player = Player(hitpoints=10, mana=250)
boss = Boss(hitpoints=20, damage=8)

spells = [
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, healing=2),
    Spell("Shield", 113, armor=7, duration=6),
    Spell("Poison", 173, damage=3, duration=6),
    Spell("Recharge", 229, mana=101, duration=5)
]

best_mana_cost, best_sequence = find_least_mana_sequence(player, boss, spells)
print(f"Least mana cost: {best_mana_cost}")
print("Best spell sequence:")
for spell in best_sequence:
    print(spell.name)
