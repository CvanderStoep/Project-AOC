import re
import hashlib
import time
from functools import lru_cache


@lru_cache(maxsize=1000)
def md5_hash_string(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Retrieve the hexadecimal digest of the hash
    return md5_hash.hexdigest()


@lru_cache(maxsize=1000)
def multiple_hash(input_string):
    for _ in range(2017):
        input_string = md5_hash_string(input_string)
    return input_string


def find_three_consecutive(s):
    # Search for three consecutive identical characters
    match = re.search(r'(.)\1\1', s)
    if match:
        return match.group(0)  # Return the matching characters
    return None


def find_five_consecutive(s):
    # Search for five consecutive identical characters
    match = re.search(r'(.)\1\1\1\1', s)
    if match:
        return match.group(0)  # Return the matching characters
    return None


def compute(hash_function) -> str:
    salt = 'yjdafjpo'

    total_keys = 0
    i = 0
    while total_keys < 64:
        i += 1
        key = salt + str(i)
        hash_value = hash_function(key)
        tree_string = find_three_consecutive(hash_value)
        if tree_string is not None:
            for j in range(i + 1, i + 1001):
                key = salt + str(j)
                hash_value = hash_function(key)
                five_string = find_five_consecutive(hash_value)
                if five_string is not None and tree_string in five_string:
                    total_keys += 1
                    print(total_keys, i, j, tree_string, five_string)
                    break

    return f'64th key at index {i}'


if __name__ == '__main__':
    start_time = time.time()
    print(f"Part I: {compute(md5_hash_string)}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function I took {execution_time:.2f} seconds to execute.")

    start_time = time.time()
    print(f"Part II: {compute(multiple_hash)}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function II took {execution_time:.2f} seconds to execute.")
