import re

f = open("2024/input/5.txt").read()
f1 = open("2024/input/5.txt").readlines()

rules = re.findall(r"(\d\d)\|(\d\d)", f, re.DOTALL)

updates = []
for line in f1:
    if "," in line:
        updates += [re.findall(r"(\d\d)", line)]


# Check each update if it matches the rules
to_fix = []
for u in updates:
    for r in rules:
        try:
            a = u.index(r[0])
            b = u.index(r[1])
            if b < a:
                to_fix += [u]
                break
        except:
            pass

middles = 0
for u in to_fix:
    fixing = True
    while fixing:
        fixing = False
        for r in rules:
            try:
                a = u.index(r[0])
                b = u.index(r[1])
                if b < a:
                    u[a], u[b] = u[b], u[a]
                    fixing = True
            except:
                pass
    middles += int(u[len(u) // 2])


print(middles)
