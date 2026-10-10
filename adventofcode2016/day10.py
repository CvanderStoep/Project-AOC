import re
from collections import deque
from dataclasses import dataclass
from typing import Union


@dataclass
class Bot:
    number: int
    chip1: int = None
    chip2: int = None
    low: Union['Bot', 'Output'] = None
    high: Union['Bot', 'Output'] = None


@dataclass
class Output:
    number: int
    chip: int = None


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_instruction(instruction: str, bots: dict, output_bin: dict) -> None:
    if 'value' in instruction:
        chip, bot_number = map(int, re.findall(r'\d+', instruction))
        bot = bots[bot_number]
        if bot.chip1 is None:
            bot.chip1 = chip
        else:
            bot.chip2 = chip
    else:
        _, bot_number, _, _, _, low_output, nl, _, _, _, high_output, nh = instruction.split(' ')
        bot_number, nl, nh = int(bot_number), int(nl), int(nh)
        bot = bots[bot_number]
        if low_output == 'bot':
            bot.low = bots[nl]
        else:
            bot.low = output_bin[nl]
        if high_output == 'bot':
            bot.high = bots[nh]
        else:
            bot.high = output_bin[nh]


def process_bots(bots: dict, output_bin: dict) -> int:
    queue = deque()
    for key, bot in bots.items():
        if bot.chip1 is not None and bot.chip2 is not None:
            queue.append(bot)

    bot_number = -1
    while queue:
        bot = queue.pop()
        lower_chip = min(bot.chip1, bot.chip2)
        higher_chip = max(bot.chip1, bot.chip2)
        recipient = bot.low
        if lower_chip == 17 and higher_chip == 61:
            bot_number = bot.number
        if isinstance(recipient, Bot):
            if recipient.chip1 is None:
                recipient.chip1 = lower_chip
            else:
                recipient.chip2 = lower_chip
                queue.append(recipient)
        else:
            recipient.chip = lower_chip
        recipient = bot.high
        if isinstance(recipient, Bot):
            if recipient.chip1 is None:
                recipient.chip1 = higher_chip
            else:
                recipient.chip2 = higher_chip
                queue.append(recipient)
        else:
            recipient.chip = higher_chip

        bot.chip1 = None
        bot.chip2 = None

    return bot_number


def count_bots(instructions: list) -> int:
    number_bots = 0
    for instruction in instructions:
        if 'value' not in instruction:
            n = int(instruction.split(' ')[1])
            number_bots = max(number_bots, n)
    return number_bots + 1


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    print(instructions)
    number_bots = count_bots(instructions)

    bots = dict()
    output_bin = dict()
    for i in range(number_bots):
        bots[i] = Bot(number=i)
        output_bin[i] = Output(number=i)

    for instruction in instructions:
        process_instruction(instruction, bots, output_bin)

    bot_number = process_bots(bots, output_bin)

    return f'{bot_number= }'


def compute_part_two(file_name: str) -> str:
    instructions = read_input_file(file_name)
    number_bots = count_bots(instructions)

    bots = dict()
    output_bin = dict()
    for i in range(number_bots):
        bots[i] = Bot(number=i)
        output_bin[i] = Output(number=i)

    for instruction in instructions:
        process_instruction(instruction, bots, output_bin)

    process_bots(bots, output_bin)

    multiply_value = output_bin[0].chip * output_bin[1].chip * output_bin[2].chip

    return f'{multiply_value= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input10.txt')}")
    print(f"Part II: {compute_part_two('input/input10.txt')}")
