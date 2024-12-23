f = open("2024/input/4.txt").readlines()
f = [line.strip() for line in f]
xmas = "XMAS"

count = 0

for i in range(len(f)):
    for j in range(len(f)):
        # Count horizontal
        if j + 3 < len(f):
            t = f[i][j] + f[i][j + 1] + f[i][j + 2] + f[i][j + 3]
            count += t.count(xmas) + t.count("".join(reversed(xmas)))

        # Count vertical
        if i - 3 >= 0:
            t = f[i][j] + f[i - 1][j] + f[i - 2][j] + f[i - 3][j]
            count += t.count(xmas) + t.count("".join(reversed(xmas)))

        # Count upper right
        if i - 3 >= 0 and j + 3 < len(f):
            t = f[i][j] + f[i - 1][j + 1] + f[i - 2][j + 2] + f[i - 3][j + 3]
            count += t.count(xmas) + t.count("".join(reversed(xmas)))

        # Count upper left
        if i - 3 >= 0 and j - 3 >= 0:
            t = f[i][j] + f[i - 1][j - 1] + f[i - 2][j - 2] + f[i - 3][j - 3]
            count += t.count(xmas) + t.count("".join(reversed(xmas)))

print(count)
