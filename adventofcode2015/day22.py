# this code is not ready yet; use day22-github instead.
from dataclasses import dataclass
import gc


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    # content = list(map(int, content))

    return content


@dataclass
class Effect:
    name: str
    cost: int = 0
    damage: int = 0
    healing: int = 0
    timer: int = 0
    armor: int = 0
    mana: int = 0
    new_spell: bool = True


@dataclass
class Player:
    name: str
    hitpoints: int = 0
    armor: int = 0
    mana: int = 0
    damage: int = 0


missile = Effect("missile", cost=53, damage=4, healing=0, timer=0)
drain = Effect("drain", cost=73, damage=2, healing=2, timer=0)
shield = Effect("shield", cost=113, armor=7, timer=6)
poison = Effect('poison', cost=173, damage=3, timer=6)
recharge = Effect("recharge", cost=229, mana=101, timer=5)


def get_objects_by_class(cls):
    return [obj for obj in gc.get_objects() if isinstance(obj, cls)]


gc.collect()
effects = get_objects_by_class(Effect)
# print(effects)


def cast_spell(player: Player, boss: Player, effect=Effect) -> int:
    # todo return status of player and boss:
    # return who is dead and alive
    # return -1 if player is dead
    # return 1 if boss is dead
    # return 0 otherwise
    if effect:
        if effect.new_spell:
            effect.new_spell = False
            player.mana -= effect.cost
            if player.mana < 0:
                print('no mana available')
                return -1
        player.armor += effect.armor
        player.hitpoints -= effect.healing
        player.mana += effect.mana
        boss.hitpoints -= max(1, effect.damage)
        effect.timer -= 1
        if player.hitpoints < 0:
            return -1
        if boss.hitpoints < 0:
            return 1
    return 0


def boss_attack(player: Player, boss: Player) -> None:
    # return who is dead and alive
    # return -1 if player is dead
    # return 1 if boss is dead
    # return 0 otherwise

    player.hitpoints -= max(1, boss.damage - player.armor)


def compute_part_one(file_name: str) -> int:
    player = Player('player', hitpoints=10, mana=250)
    boss = Player('boss', hitpoints=13, damage=8)

    spell_sequence = [poison, missile] #, shield, recharge, drain]
    running_spells = []
    # TODO implement effect during multiple play round
    # put the effects in a stack, that take care of older effects
    # add new effect to the stack as well
    for effect in spell_sequence:
        # print(f'{running_spells= }')
        next_running_spells = []
        print('player turn')
        print('Player', player.hitpoints, player.armor, player.mana)
        print('Boss', boss.hitpoints)
        running_spells.append(effect)
        for spell in running_spells:
            # a running spell does not cost any mana; fixed.
            print(spell.name)
            cast_spell(player, boss, spell)
            if spell.timer > 0:
                next_running_spells.append(spell)
            else:
                print('timer = 0')
        running_spells = next_running_spells.copy()
        print('boss turn')

        print(player.hitpoints, player.armor, player.mana)
        print(boss.hitpoints)
        boss_attack(player, boss)

    return "part 1 not yet implemented"


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input0.txt')}")
    print(f"Part II: {compute_part_two('input/input0.txt')}")
