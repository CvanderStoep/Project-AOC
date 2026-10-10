def count_non_primes():
    a = 1
    b = 99 * 100 + 100000
    c = b + 17000
    h = 0

    for n in range(b, c + 1, 17):  # iterating through the range with step size 17
        if not is_prime(n):
            h += 1

    return h

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Final value in register h
print(count_non_primes())
