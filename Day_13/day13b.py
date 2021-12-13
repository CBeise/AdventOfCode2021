import re

with open("input.txt") as data_file:
    data = data_file.read().splitlines()

directions = []
for i in data:
    if i == "":
        pass
    elif i[0] == "f":
        directions.append(i)
        del i

for i in range(len(directions) + 1):
    data.pop()

instructions = []

for i in directions:
    elem = (re.findall(r'(\w+)=(\d+)', i))
    holder = [elem[0][0], int(elem[0][1])]
    instructions.append(holder)

x_max = 0
y_max = 0

for i in range(len(data)):
    data[i] = data[i].split(",")
    for j in range(2):
        data[i][j] = int(data[i][j])
    if data[i][0] > x_max:
        x_max = data[i][0]
    if data[i][1] > y_max:
        y_max = data[i][1]

grid = []

for i in range(x_max + 1):
    line = []
    for j in range(y_max + 1):
        line.append(0)
    grid.append(line)

for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    grid[x][y] += 1

del data_file, elem, holder, directions, data, x, y, j

for i in range(len(instructions)):
    fold = instructions[i]
    # Vertical fold
    if fold[0] == 'y':
        for j in range(x_max + 1):
            counter = 1
            for k in range(fold[1] + 1, y_max + 1):
                if grid[j][k] > 0:
                    grid[j][fold[1] - counter] += 1
                counter += 1
        y_max = fold[1] - 1
        for j in range(x_max + 1):
            grid[j] = grid[j][:y_max + 1]
    # Horizontal fold
    else:
        for j in range(y_max + 1):
            counter = 1
            for k in range(fold[1] + 1, x_max + 1):
                if grid[k][j] > 0:
                    grid[fold[1] - counter][j] += 1
                counter += 1
        x_max = fold[1] - 1
        grid = grid[:x_max + 1]

total = 0

for i in range(y_max + 1):
    answer = ""
    for j in range(x_max + 1):
        if grid[j][i] > 0:
            answer += "X"
        else:
            answer += " "
    print(answer)
