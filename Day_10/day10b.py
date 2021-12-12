with open("input.txt") as data_file:
    data = data_file.read().splitlines()


class Grid:
    """
    This creates a Grid object
    """
    def __init__(self, width, height):
        self.grid = []
        self.basins = []
        self.height = height
        self.width = width

    def add_row(self, row):
        self.grid.append(row)

    def create_basin_helper(self, row, column, size):
        """This method checks if the current space is available to create a new basin and if so, creates one"""
        if self.grid[row][column].available:
            self.grid[row][column].available = False
            size += 1
            if row > 0:
                size = self.create_basin_helper(row - 1, column, size)
            if row < self.height - 1:
                size = self.create_basin_helper(row + 1, column, size)
            if column > 0:
                size = self.create_basin_helper(row, column - 1, size)
            if column < self.width - 1:
                size = self.create_basin_helper(row, column + 1, size)
        return size

    def create_basin(self, row, column):
        size = 0
        if self.grid[row][column].available:
            size = self.create_basin_helper(row, column, size)
        if size > 0:
            self.basins.append(size)


class Space:
    """
    This creates a Space object
    """
    def __init__(self, height):
        self.height = height
        if self.height == 9:
            self.available = False
        else:
            self.available = True


grid = Grid(len(data), len(data[0]))

for i in range(len(data)):
    line = []
    for j in range(len(data[i])):
        line.append(Space(int(data[i][j])))
    grid.add_row(line)

for i in range(grid.height):
    for j in range(grid.width):
        grid.create_basin(i, j)

basins = sorted(grid.basins, reverse=True)

result = basins[0] * basins[1] * basins[2]

print(result)
