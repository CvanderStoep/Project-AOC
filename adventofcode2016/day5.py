import time
import random
import sys
import hashlib


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def md5_hash_string(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Retrieve the hexadecimal digest of the hash
    return md5_hash.hexdigest()


def decrypt_animation(encrypted_text, decrypted_text):
    # Clear the output
    def clear_output():
        sys.stdout.write('\r' + ' ' * len(encrypted_text) + '\r')

    # Create a pool of possible characters
    pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for i in range(len(decrypted_text)):
        for _ in range(10):  # Simulate multiple attempts
            clear_output()
            # Randomly replace each character with a character from the pool
            intermediate_text = encrypted_text[:i] + ''.join(
                random.choice(pool) for _ in range(len(decrypted_text) - i))
            sys.stdout.write(intermediate_text)
            sys.stdout.flush()
            time.sleep(0.05)

        # Set the correct character at position i
        encrypted_text = encrypted_text[:i] + decrypted_text[i] + encrypted_text[i + 1:]
        clear_output()
        sys.stdout.write(encrypted_text)
        sys.stdout.flush()
        time.sleep(0.1)


def compute_part_one(file_name: str) -> str:
    i = 0
    password = ''
    encrypted_text = "--------"

    while True:
        input_string = 'cxdnnyjw' + str(i)
        hash_value = md5_hash_string(input_string)
        if hash_value.startswith("00000"):
            password = password + hash_value[5]
            decrypt_animation(encrypted_text, password)
            if len(password) == 8:
                break
        i += 1
    print('')

    return f'{password= }'


def compute_part_two(file_name: str) -> str:
    i = 0
    password = ['-'] * 8
    encrypted_text = "--------"

    while True:
        input_string = 'cxdnnyjw' + str(i)
        hash_value = md5_hash_string(input_string)
        if hash_value.startswith("00000"):
            value = hash_value[6]
            position = hash_value[5]
            if position in '01234567':
                position = int(position)
                if password[position] == '-':
                    password[position] = value
                    decrypted_text = ''.join(password)
                    decrypt_animation(encrypted_text, decrypted_text)
                if '-' not in password:
                    break
        i += 1
    password = ''.join(password)
    print('')

    return f'{password= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input0.txt')}")
    print(f"Part II: {compute_part_two('input/input0.txt')}")
