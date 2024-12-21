import re

f = open("2024/input/3.txt").read()
f = "do()" + f + "don't()"
result = 0
m = re.findall(r"do\(\)(.+?)don't\(\)", f, re.DOTALL)
print(m[-1])

for instruction in m:
    n = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
    result += sum([int(a[0]) * int(a[1]) for a in n])

print(result)
