import itertools
import re
from dataclasses import dataclass
import gc


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Weapon(Item):
    pass


@dataclass
class Armor(Item):
    pass


@dataclass
class Ring(Item):
    pass


@dataclass
class Player:
    name: str
    hitpoints: int
    damage: int
    armor: int


dagger = Weapon('dagger', 8, 4, 0)
shortsword = Weapon('shortsword', 10, 5, 0)
warhammer = Weapon('warhammer', 25, 6, 0)
longsword = Weapon('longsword', 40, 7, 0)
greataxe = Weapon('greataxe', 74, 8, 0)

leather = Armor('leather', 13, 0, 1)
chainmail = Armor('chainmail', 31, 0, 2)
splintmail = Armor('splintmail', 53, 0, 3)
bandedmail = Armor('bandedmail', 75, 0, 4)
platemail = Armor('platemail', 102, 0, 5)

damage1 = Ring('damage1', 25, 1, 0)
damage2 = Ring('damage2', 50, 2, 0)
damage3 = Ring('damage3', 100, 3, 0)
damage_1 = Ring('damage_1', 20, 0, 1)
damage_2 = Ring('damage_2', 40, 0, 2)
damage_3 = Ring('damage_3', 80, 0, 3)

# weapons = [dagger, shortsword, warhammer, longsword, greataxe]
# armors = [leather, chainmail, splintmail, bandedmail, platemail]
# rings = [damage1, damage2, damage3, damage_1, damage_2, damage_3]

gc.collect()


def get_objects_by_class(cls):
    return [obj for obj in gc.get_objects() if isinstance(obj, cls)]


rings = get_objects_by_class(Ring)
armors = get_objects_by_class(Armor)
weapons = get_objects_by_class(Weapon)


def upgrade_player(player: Player, item: Item) -> int:
    cost = 0
    if item:
        player.damage += item.damage
        player.armor += item.armor
        cost = item.cost
    return cost


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    stats = []
    for line in content:
        pattern = r'\d+'
        a = re.findall(pattern, line)
        stats.append(int(a[0]))

    return stats


def generate_combinations(list1, list2, list3) -> list:
    # Generate all combinations
    combinations = []

    # Include exactly 1 item from list1
    for item1 in list1:
        # Include 0 or 1 item from list2
        for item2 in itertools.chain([None], list2):
            # Include 0, 1, or 2 items from list3
            for item3_comb in itertools.chain.from_iterable(itertools.combinations(list3, r) for r in range(3)):
                combo = [item1]
                if item2 is not None:
                    combo.append(item2)
                combo.extend(item3_comb)
                combinations.append(combo)

    return combinations


def play_game(boss: Player, player: Player) -> bool:
    def play_game_round(player1: Player, player2: Player) -> (Player, Player):
        player2.hitpoints -= max(1, player1.damage - player2.armor)
        player1.hitpoints -= max(1, player2.damage - player1.armor)
        return player1, player2

    # returns True is player wins, otherwise False
    while boss.hitpoints > 0 and player.hitpoints > 0:
        player, boss = play_game_round(player, boss)
        if boss.hitpoints <= 0:
            return True
        if player.hitpoints <= 0:
            return False


def compute_part_one(file_name: str) -> int:
    hit, damage, armor = read_input_file(file_name)

    combinations = generate_combinations(weapons, armors, rings)
    minimum_cost_to_win = float('inf')
    for combination in combinations:
        player = Player('player', 100, 0, 0)
        boss = Player('boss', hit, damage, armor)
        cost = 0
        for item in combination:
            cost += upgrade_player(player, item)
        player_wins = play_game(boss, player)
        if player_wins:
            minimum_cost_to_win = min(cost, minimum_cost_to_win)
    print(f'{minimum_cost_to_win= }')

    return minimum_cost_to_win


def compute_part_two(file_name: str) -> int:
    hit, damage, armor = read_input_file(file_name)

    combinations = generate_combinations(weapons, armors, rings)
    maximum_cost_to_loose = 0
    for combination in combinations:
        player = Player('player', 100, 0, 0)
        boss = Player('boss', hit, damage, armor)
        cost = 0
        for item in combination:
            cost += upgrade_player(player, item)
        player_wins = play_game(boss, player)
        if not player_wins:
            maximum_cost_to_loose = max(cost, maximum_cost_to_loose)
    print(f'{maximum_cost_to_loose= }')

    return maximum_cost_to_loose


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input21.txt')}")
    print(f"Part II: {compute_part_two('input/input21.txt')}")
