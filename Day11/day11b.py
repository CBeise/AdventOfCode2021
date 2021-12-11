class Octopus:
    """
    This class creates an Octopus object
    """

    def __init__(self, power):
        self.power = power
        self.flashed = False
        self.flashes = 0

    def power_up(self):
        """This increases the power level of the Octopus, if it has not yet flashed this step"""
        if self.flashed:
            return False
        elif self.power == 9:
            self.flashes += 1
            self.flashed = True
            self.power = 0
        else:
            self.power += 1
        return self.flashed

    def count_flashes(self):
        """This returns the number of times the Octopus has flashed"""
        return self.flashes


class Grid:
    """
    This creates a Grid object
    """
    def __init__(self):
        self.grid = []

    def add_row(self, row):
        self.grid.append(row)

    def increase_energy(self):
        """This increases the energy level of all Octopus objects in the Grid"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].power_up():
                    self.check_adjacent(i, j)

    def check_adjacent(self, row, column):
        """This method is called when an Octopus flashes, it then increases the surrounding Octopuss's, Octopus',
        Octopi's? energy levels by 1, unless they have already flashed this step."""
        # If the Octopus is in the top row of the grid
        if row == 0:
            if self.grid[row + 1][column].power_up():
                self.check_adjacent(row + 1, column)
            # If the Octopus is in the top left corner of the grid
            if column == 0:
                if self.grid[row][column + 1].power_up():
                    self.check_adjacent(row, column + 1)
                if self.grid[row + 1][column + 1].power_up():
                    self.check_adjacent(row + 1, column + 1)
            else:
                if self.grid[row][column - 1].power_up():
                    self.check_adjacent(row, column - 1)
                if self.grid[row + 1][column - 1].power_up():
                    self.check_adjacent(row + 1, column - 1)
                # If the Octopus is in the top row, but not in a corner
                if column != 9:
                    if self.grid[row][column + 1].power_up():
                        self.check_adjacent(row, column + 1)
                    if self.grid[row + 1][column + 1].power_up():
                        self.check_adjacent(row + 1, column + 1)
        # If the Octopus is in the bottom row of the grid
        elif row == 9:
            if self.grid[row - 1][column].power_up():
                self.check_adjacent(row - 1, column)
            # If the Octopus is in the bottom left corner of the grid
            if column == 0:
                if self.grid[row][column + 1].power_up():
                    self.check_adjacent(row, column + 1)
                if self.grid[row - 1][column + 1].power_up():
                    self.check_adjacent(row - 1, column + 1)
            else:
                if self.grid[row][column - 1].power_up():
                    self.check_adjacent(row, column - 1)
                if self.grid[row - 1][column - 1].power_up():
                    self.check_adjacent(row - 1, column - 1)
                # If the Octopus is in the top row, but not in a corner
                if column != 9:
                    if self.grid[row][column + 1].power_up():
                        self.check_adjacent(row, column + 1)
                    if self.grid[row - 1][column + 1].power_up():
                        self.check_adjacent(row - 1, column + 1)
        else:
            if self.grid[row - 1][column].power_up():
                self.check_adjacent(row - 1, column)
            if self.grid[row + 1][column].power_up():
                self.check_adjacent(row + 1, column)
            # If the Octopus is in the first column of the grid:
            if column == 0:
                if self.grid[row][column + 1].power_up():
                    self.check_adjacent(row, column + 1)
                if self.grid[row - 1][column + 1].power_up():
                    self.check_adjacent(row - 1, column + 1)
                if self.grid[row + 1][column + 1].power_up():
                    self.check_adjacent(row + 1, column + 1)
            else:
                if self.grid[row][column - 1].power_up():
                    self.check_adjacent(row, column - 1)
                if self.grid[row - 1][column - 1].power_up():
                    self.check_adjacent(row - 1, column - 1)
                if self.grid[row + 1][column - 1].power_up():
                    self.check_adjacent(row + 1, column - 1)
                if column != 9:
                    if self.grid[row][column + 1].power_up():
                        self.check_adjacent(row, column + 1)
                    if self.grid[row - 1][column + 1].power_up():
                        self.check_adjacent(row - 1, column + 1)
                    if self.grid[row + 1][column + 1].power_up():
                        self.check_adjacent(row + 1, column + 1)

    def reset_flash(self):
        """This resets the flashed flag at the end of every step."""
        counter = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].flashed:
                    counter += 1
                    self.grid[i][j].flashed = False
        if counter == 100:
            return True
        else:
            return False

    def check_flashes(self):
        """This counts the number of times the occupants of the grid have flashed"""
        total = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                total += self.grid[i][j].count_flashes()
        return total


with open("input.txt") as data_file:
    data = data_file.read().splitlines()

grid = Grid()

# Populate the grid with Octopus objects
for i in range(len(data)):
    line = []
    for j in range(len(data[i])):
        line.append(Octopus(int(data[i][j])))
    grid.add_row(line)

# Simulate until we get a MEGA FLASH!
mega_flash = False
step = 1
while not mega_flash:
    grid.increase_energy()
    if grid.reset_flash():
        print("MEGA FLASH ALERT!!!! , STEP: ", step)
        mega_flash = True
    step += 1

flashes = grid.check_flashes()

print(flashes)
