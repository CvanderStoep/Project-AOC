def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    # content = list(map(int, content))

    return content


def is_string_nice(string: str) -> bool:
    def count_vowels(string: str) -> int:
        vowels = "aeiou"
        count = 0
        for char in string:
            if char.lower() in vowels:
                count += 1
        return count

    def has_consecutive_identical_letters(string: str) -> bool:
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return True
        return False

    def has_specific_pattern(string: str) -> bool:
        patterns = ['ab', 'cd', 'pq', 'xy']
        for pattern in patterns:
            if pattern in string:
                return True
        return False

    count = count_vowels(string)
    if (count >= 3) and not has_specific_pattern(string) and has_consecutive_identical_letters(string):
        return True
    return False


def is_string_nice_two(string: str) -> bool:
    def has_repeating_pair(s):
        for i in range(len(s) - 1):
            pair = s[i:i + 2]
            if pair in s[i + 2:]:
                return True
        return False

    def has_repeating_letter_with_one_between(s):
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                return True
        return False

    if has_repeating_pair(string) and has_repeating_letter_with_one_between(string):
        return True
    return False


def compute_part(file_name: str, function) -> int:
    content = read_input_file(file_name)
    number_of_nice_strings = 0
    for string in content:
        if function(string):
            number_of_nice_strings += 1

    return number_of_nice_strings


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input5.txt', is_string_nice)}")
    print(f"Part II: {compute_part('input/input5.txt', is_string_nice_two)}")
