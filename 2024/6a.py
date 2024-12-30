g = open("2024/input/6.txt").readlines()
g = [i.strip() for i in g]
f = []
for i in g:
    line = []
    for j in i:
        line += [j]
    f += [line]


def move(direction, location):
    if direction == "up":
        return (location[0] - 1, location[1])
    if direction == "down":
        return (location[0] + 1, location[1])
    if direction == "left":
        return (location[0], location[1] - 1)
    if direction == "right":
        return (location[0], location[1] + 1)


def check(direction, location):
    if direction == "up":
        if in_bounds((location[0] - 1, location[1])):
            return f[location[0] - 1][location[1]] != "#"
        return True
    if direction == "down":
        if in_bounds((location[0] + 1, location[1])):
            return f[location[0] + 1][location[1]] != "#"
        return True
    if direction == "left":
        if in_bounds((location[0], location[1] - 1)):
            return f[location[0]][location[1] - 1] != "#"
        return True
    if direction == "right":
        if in_bounds((location[0], location[1] + 1)):
            return f[location[0]][location[1] + 1] != "#"
        return True
    return False


def in_bounds(guard):
    if guard[0] < 0 or guard[1] < 0 or guard[0] >= len(f) or guard[1] >= len(f[0]):
        return False
    return True


def switch_direction(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"


for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == "^":
            guard = (i, j)

direction = "up"

while in_bounds(guard):
    f[guard[0]][guard[1]] = "X"
    if check(direction, guard):
        guard = move(direction, guard)
    else:
        direction = switch_direction(direction)

count = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == "X":
            count += 1

print(count)
