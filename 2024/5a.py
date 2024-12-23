import re

f = open("2024/input/5.txt").read()
f1 = open("2024/input/5.txt").readlines()

rules = re.findall(r"(\d\d)\|(\d\d)", f, re.DOTALL)

updates = []
for line in f1:
    if "," in line:
        updates += [re.findall(r"(\d\d)", line)]

# Check each update if it matches the rules
middles = 0
for u in updates:
    valid = True
    for r in rules:
        try:
            a = u.index(r[0])
            b = u.index(r[1])
            if b < a:
                valid = False
        except:
            pass
    if valid:
        middles += int(u[len(u) // 2])

print(middles)
