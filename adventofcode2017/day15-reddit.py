def AG():
    x = 591
    while True:
        x *= 16807
        x %= 2147483647
        if x % 4 == 0:
            yield x


def BG():
    x = 393
    while True:
        x *= 48271
        x %= 2147483647
        if x % 8 == 0:
            yield x


A = AG()
B = BG()
matches = 0
for i in range(5_000_000):
    a = next(A)
    b = next(B)
    if a & 0xFFFF == b & 0xFFFF:
        matches += 1
print(matches)