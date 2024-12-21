import re

f = open("2024/input/3.txt").readlines()

result = 0
for line in f:
    m = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    result += sum([int(a[0]) * int(a[1]) for a in m])

print(result)
