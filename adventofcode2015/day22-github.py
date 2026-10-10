import re
from copy import deepcopy

# Define the input file path
fn = 'input/input22.txt'

# Define the spell list with details for each spell
spell_list = [
    {'name': 'missile', 'cost': 53, 'damage': 4, 'armor': 0, 'heal': 0, 'mana': 0, 'time': 1},
    {'name': 'drain', 'cost': 73, 'damage': 2, 'armor': 0, 'heal': 2, 'mana': 0, 'time': 1},
    {'name': 'shield', 'cost': 113, 'damage': 0, 'armor': 7, 'heal': 0, 'mana': 0, 'time': 6},
    {'name': 'poison', 'cost': 173, 'damage': 3, 'armor': 0, 'heal': 0, 'mana': 0, 'time': 6},
    {'name': 'recharge', 'cost': 229, 'damage': 0, 'armor': 0, 'heal': 0, 'mana': 101, 'time': 5},
]


# Function to apply active spell effects
def apply_effects(player, boss):
    active = player['active']
    current_armor = 0

    for idx, spell in enumerate(spell_list):
        if active[idx] > 0:
            boss['hp'] -= spell['damage']
            player['hp'] += spell['heal']
            player['mana'] += spell['mana']
            current_armor += spell['armor']
            active[idx] -= 1

    return current_armor


# Function to play the game and return mana used to win
def play_game(start_boss, hard_mode=False):
    # Initialize player and boss states
    start_player = {
        'hp': 50,
        'mana': 500,
        'total': 0,
        'active': [0, 0, 0, 0, 0]
    }
    # Queue to store game states
    state_queue = [('player', deepcopy(start_boss), deepcopy(start_player))]
    best_mana_cost = float('inf')

    while state_queue:
        turn, boss, player = state_queue.pop()

        # Prune branches that exceed the best mana cost
        if player['total'] >= best_mana_cost:
            continue

        if turn == 'player':
            if hard_mode:  # Apply hard mode penalty
                player['hp'] -= 1
                if player['hp'] <= 0:
                    continue

            # Apply spell effects and check if boss is dead
            apply_effects(player, boss)
            if boss['hp'] <= 0:
                best_mana_cost = min(player['total'], best_mana_cost)
                continue

            # Cast spells if possible
            for idx, spell in enumerate(spell_list):
                if player['active'][idx] == 0 and player['mana'] >= spell['cost']:
                    new_player = deepcopy(player)
                    new_player['mana'] -= spell['cost']
                    new_player['total'] += spell['cost']
                    new_player['active'][idx] = spell['time']
                    print(player)
                    print(new_player)
                    print('--')
                    state_queue.append(('boss', deepcopy(boss), new_player))

        else:  # Boss's turn
            # Apply spell effects and check if boss is dead
            current_armor = apply_effects(player, boss)
            if boss['hp'] <= 0:
                best_mana_cost = min(player['total'], best_mana_cost)
                continue

            # Boss attacks player
            player['hp'] -= max(1, boss['damage'] - current_armor)
            if player['hp'] <= 0:
                continue

            # Queue the next player turn
            state_queue.append(('player', deepcopy(boss), deepcopy(player)))

    return best_mana_cost


# Read input file and parse boss's hit points and damage
with open(fn, 'r') as file:
    hp, damage = map(int, (re.findall(r'\d+', line)[0] for line in file))
    boss = {'hp': hp, 'damage': damage}

# Calculate and print the least amount of mana needed to win
print(f"Part 1: Least mana used is {play_game(boss, hard_mode=False)}")
print(f"Part 2: Least mana used is {play_game(boss, hard_mode=True)}")
