f = open("2024/input/2.txt").readlines()


def safe(r):
    safe = r == sorted(r) or r == list(reversed(sorted(r)))

    for i in range(len(r) - 1):
        safe &= abs(r[i] - r[i + 1]) >= 1 and abs(r[i] - r[i + 1]) <= 3

    return safe


result = 0
for r in f:
    r = [int(l) for l in r.split()]
    for i in range(len(r)):
        t = [r[j] for j in range(len(r)) if j != i]
        if safe(t):
            result += 1
            break

print(result)
