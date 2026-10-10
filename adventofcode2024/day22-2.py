file = open("input/input22.txt")
l = file.read().split("\n")
file.close()

l = [int(j) for j in l]

d = {}
for x in l:
    seq = []
    # x = b
    seen = set()
    for i in range(2000):
        y = x
        x = (x ^ (x * 64)) % 16777216
        x = (x ^ (x // 32)) % 16777216
        x = (x ^ (x * 2048)) % 16777216

        # if i == -1:
        #     pass
        #     # seq = [x % 10] # corrected from the original solution
        # else:
        seq = seq + [x % 10 - y % 10]
        if len(seq) > 4:
            seq = seq[1:]

        key = tuple(seq)
        if len(key) == 4 and key not in seen:
            d[key] = d.get(key, 0) + (x % 10)
            seen.add(key)

max_key = max(d, key = d.get)
max_value = d[max_key]
print(max(d.values()))
print(max_key, max_value)
print(len(d))