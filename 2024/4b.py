f = open("2024/input/4.txt").readlines()
f = [line.strip() for line in f]
mas = "MAS"

count = 0

for i in range(len(f)):
    for j in range(len(f)):
        try:
            t = f[i][j] + f[i + 1][j + 1] + f[i + 2][j + 2]
            t1 = f[i + 2][j] + f[i + 1][j + 1] + f[i][j + 2]
            t_count = (
                t.count(mas)
                + t.count("".join(reversed(mas)))
                + t1.count(mas)
                + t1.count("".join(reversed(mas)))
            )
            count += 1 if t_count > 1 else 0
        except:
            pass


print(count)
# 3561 too high
