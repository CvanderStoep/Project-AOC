def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        # Read lines and split each line into a list of words
        content = [line.split() for line in f.read().splitlines()]
    return content


def check_passphrase(phrase: list[str]) -> bool:
    # check for double words by converting the list to a set
    return len(phrase) == len(set(phrase))


def check_passphrase_anagram(phrase: list[str]) -> bool:
    # check for anagrams, aba & baa are identical
    condensed_phrase = [''.join(sorted(word)) for word in phrase]
    return check_passphrase(condensed_phrase)


def compute_part(file_name: str, passphrase_function) -> str:
    phrases = read_input_file(file_name)

    valid_phrases = sum(1 for phrase in phrases if passphrase_function(phrase))

    return f'{valid_phrases= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input4.txt', check_passphrase)}")
    print(f"Part II: {compute_part('input/input4.txt', check_passphrase_anagram)}")
