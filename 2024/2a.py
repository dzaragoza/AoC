f = open("2024/input/2.txt").readlines()

result = 0
for r in f:
    r = [int(l) for l in r.split()]
    safe = r == sorted(r) or r == list(reversed(sorted(r)))

    for i in range(len(r) - 1):
        safe &= abs(r[i] - r[i + 1]) >= 1 and abs(r[i] - r[i + 1]) <= 3

    result += 1 if safe else 0

print(result)
