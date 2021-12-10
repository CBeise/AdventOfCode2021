with open("input.txt") as input_file:
    data = input_file.read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split("|")

for i in range(len(data)):
    for j in range(2):
        data[i][j] = data[i][j].split()

numbers = 0

for i in range(len(data)):
    for j in data[i][1]:
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            numbers += 1


