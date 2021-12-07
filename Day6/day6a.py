import re

with open("input.txt") as coordinate_file:
    numbers = list(map(int, re.findall('\d+', coordinate_file.read())))

print(len(numbers))
print(numbers)

for j in range(80):
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 6
            numbers.append(8)
        else:
            numbers[i] -= 1

print(len(numbers))


