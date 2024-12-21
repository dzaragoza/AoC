f = open("2024/input/1.txt").readlines()
a = sorted([int(i.split()[0]) for i in f])
b = sorted([int(i.split()[1]) for i in f])

result = sum(abs(a[i] - b[i]) for i in range(len(a)))
print(result)
