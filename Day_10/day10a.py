with open("input.txt") as data_file:
    data = data_file.read().splitlines()

grid = []

for i in range(len(data)):
    row = []
    for j in range(len(data[i])):
        row.append(int(data[i][j]))
    grid.append(row)

risk = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        cur = grid[i][j]
        if i == 0:
            if j == 0:
                if cur < grid[i][j + 1] and cur < grid[i + 1][j]:
                    risk += cur + 1
            elif j == len(grid[i]) - 1:
                if cur < grid[i][j - 1] and cur < grid[i + 1][j]:
                    risk += cur + 1
            elif cur < grid[i][j + 1] and cur < grid[i][j - 1] and cur < grid[i + 1][j]:
                risk += cur + 1
        elif i == len(grid) - 1:
            if j == 0:
                if cur < grid[i][j + 1] and cur < grid[i - 1][j]:
                    risk += cur + 1
            elif j == len(grid[i]) - 1:
                if cur < grid[i][j - 1] and cur < grid[i - 1][j]:
                    risk += cur + 1
            elif cur < grid[i][j + 1] and cur < grid[i][j - 1] and cur < grid[i - 1][j]:
                risk += cur + 1
        elif cur < grid[i + 1][j] and cur < grid[i - 1][j]:
            if j == 0:
                if cur < grid[i][j + 1]:
                    risk += cur + 1
            elif j == len(grid[i]) - 1:
                if cur < grid[i][j - 1]:
                    risk += cur + 1
            else:
                if cur < grid[i][j + 1] and cur < grid[i][j - 1]:
                    risk += cur + 1

print(risk)
