with open("input.txt") as input_file:
    data = input_file.read().splitlines()


class Grid:
    """
    This creates a Grid object
    """
    def __init__(self):
        self.grid = []
        self.height = 0
        self.width = None
        self.end = None
        self.border = set()

    def add_row(self, row):
        self.grid.append(row)
        if self.width is None:
            self.width = len(row)
        self.height = len(self.grid)
        self.end = self.grid[self.height - 1][self.width - 1]

    def __getitem__(self, item):
        return self.grid[item]


class Space:
    """
    This creates a Space class
    """
    def __init__(self, risk, x, y):
        self.risk = risk
        self.x_val = x
        self.y_val = y
        self.distance = None
        self.neighbors = {"up": True,
                          "down": True,
                          "left": True,
                          "right": True}


grid = Grid()

for i in range(len(data)):
    line = []
    for j in range(len(data[i])):
        line.append(Space(int(data[i][j]), i, j))
    grid.add_row(line)

for i in range(1, 5):
    for line in range(grid.width):
        row = []
        for j in range(grid.width):
            number = grid[line][j].risk + i
            if number > 9:
                number = number % 9
            row.append(Space(number, i * 100 + line, j))
        grid.add_row(row)

for line in range(grid.height):
    for i in range(1, 5):
        for j in range(grid.width):
            number = grid[line][j].risk + i
            if number > 9:
                number = number % 9
            grid[line].append(Space(number, line, i * 100 + j))

grid.width = len(grid[0])
grid.end = grid[grid.height - 1][grid.width - 1]

width = grid.width
height = grid.height

print(height, width)

for i in grid[0]:
    i.neighbors["up"] = False
for i in grid[height - 1]:
    i.neighbors["down"] = False

for i in range(width):
    grid[i][height - 1].neighbors["right"] = False
    grid[i][0].neighbors["left"] = False

grid[0][0].distance = 0

grid.border.add(grid[0][0])

safest = 9

while grid.end.distance is None:
    candidates = set()
    for i in grid.border:
        x = i.x_val
        y = i.y_val
        if i.neighbors["up"]:
            temp = grid[x-1][y]
            if temp.distance is None:
                if temp.risk + i.distance < safest:
                    safest = temp.risk + i.distance
                    candidates = {(temp, "up", i)}
                elif temp.risk + i.distance == safest:
                    candidates.add((temp, "up", i))
        if i.neighbors["down"]:
            temp = grid[x + 1][y]
            if temp.distance is None:
                if temp.risk + i.distance < safest:
                    safest = temp.risk + i.distance
                    candidates = {(temp, "down", i)}
                elif temp.risk + i.distance == safest:
                    candidates.add((temp, "down", i))
        if i.neighbors["left"]:
            temp = grid[x][y - 1]
            if temp.distance is None:
                if temp.risk + i.distance < safest:
                    safest = temp.risk + i.distance
                    candidates = {(temp, "left", i)}
                elif temp.risk + i.distance == safest:
                    candidates.add((temp, "left", i))
        if i.neighbors["right"]:
            temp = grid[x][y + 1]
            if temp.distance is None:
                if temp.risk + i.distance < safest:
                    safest = temp.risk + i.distance
                    candidates = {(temp, "right", i)}
                elif temp.risk + i.distance == safest:
                    candidates.add((temp, "right", i))
    new_border = set()
    for i in candidates:
        i[0].distance = i[2].distance + i[0].risk
        safest = i[0].distance + 9
        i[2].neighbors[i[1]] = False
        if i[1] == "down":
            i[0].neighbors["up"] = False
        elif i[1] == "up":
            i[0].neighbors["down"] = False
        elif i[1] == "left":
            i[0].neighbors["right"] = False
        elif i[1] == "right":
            i[0].neighbors["left"] = False
        for j in i[0].neighbors.keys():
            if i[0].neighbors[j]:
                new_border.add(i[0])
            if i[2].neighbors[j]:
                new_border.add(i[2])
        # print((i[0].x_val, i[0].y_val), i[0].distance)
    for i in grid.border:
        for j in i.neighbors.keys():
            if i.neighbors[j]:
                new_border.add(i)
    grid.border = new_border

print("Distance to end: ", grid.end.distance)
