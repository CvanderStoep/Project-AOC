import hashlib


def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read()

    return content


def compute_md5_hash(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()


def compute_part_one(file_name: str, number_of_leading_zeros: int = 5) -> int:
    content = read_input_file(file_name)
    secret_key = 1
    zeros = '0' * number_of_leading_zeros
    while True:
        combination = content + str(secret_key)
        hash_result = compute_md5_hash(combination)
        # if secret_key % 100000 == 0:
        #     print(f"The MD5 hash of '{combination}' is: {hash_result}")

        if hash_result.startswith(zeros):
            print(f"The MD5 hash of '{combination}' is: {hash_result}")
            break
        else:
            secret_key += 1

    return secret_key


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input4.txt', number_of_leading_zeros=5)}")
    print(f"Part II: {compute_part_one('input/input4.txt', number_of_leading_zeros=6)}")
