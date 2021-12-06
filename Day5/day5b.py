import re

with open("input.txt") as coordinate_file:
    numbers = list(map(int, re.findall('\d+', coordinate_file.read())))

x_coord, y_coord = [], []

for i in range(len(numbers)):
    if i % 2 == 0:
        x_coord.append(numbers[i])
    else:
        y_coord.append(numbers[i])

x_max = x_coord[0]
y_max = y_coord[0]

for i in range(len(x_coord)):
    if x_coord[i] > x_max:
        x_max = x_coord[i]
    if y_coord[i] > y_max:
        y_max = y_coord[i]

grid = []

for i in range(x_max + 1):
    grid.append([])
    for j in range(y_max + 1):
        grid[i].append(0)

counter = 0

while counter < len(x_coord):
    x1 = x_coord[counter]
    y1 = y_coord[counter]
    counter += 1
    x2 = x_coord[counter]
    y2 = y_coord[counter]
    counter += 1

    # Vertical
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            grid[x1][i] += 1
    # Horizontal
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            grid[i][y1] += 1
    # Diagonal
    elif x1 > x2:
        if y1 < y2:
            for i in range(x1, x2 - 1, -1):
                grid[i][y1] += 1
                y1 += 1
        else:
            for i in range(x1, x2 - 1, -1):
                grid[i][y1] += 1
                y1 -= 1
    elif y1 < y2:
        for i in range(x1, x2 + 1):
            grid[i][y1] += 1
            y1 += 1
    else:
        for i in range(x1, x2 + 1):
            grid[i][y1] += 1
            y1 -= 1


overlap = 0

for i in range(x_max):
    for j in range(y_max):
        if grid[i][j] > 1:
            overlap += 1

print(overlap)
