def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read()

    return content


def next_string(s):
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    return ''.join(s)


def contains_increasing_sequence(s):
    # Length of increasing sequences to check
    length_to_check = 3

    # Iterate over the string, checking for increasing sequences
    for i in range(len(s) - length_to_check + 1):
        if all(ord(s[i + j]) == ord(s[i]) + j for j in range(length_to_check)):
            return True
    return False


def contains_two_different_pairs(s):
    pairs = set()
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs.add(s[i])
            i += 2  # Move past the current pair
        else:
            i += 1

    return len(pairs) >= 2


def is_valid_password(password: str) -> bool:
    confusing_letters = {'i', 'o', 'l'}
    is_confusing = any(letter in password for letter in confusing_letters)
    if is_confusing:
        return False

    increasing_sequence = contains_increasing_sequence(password)
    if not increasing_sequence:
        return False

    two_different_pairs = contains_two_different_pairs(password)
    if not two_different_pairs:
        return False

    return True


def compute_part(file_name: str) -> None:
    password = read_input_file(file_name)
    print(password)
    while True:
        password = next_string(password)
        if is_valid_password(password):
            print('PartI: ', password)
            break

    while True:
        password = next_string(password)
        if is_valid_password(password):
            print('PartII: ', password)
            break


if __name__ == '__main__':
    compute_part('input/input11.txt')
