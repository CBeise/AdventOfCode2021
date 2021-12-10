import re

with open("input.txt") as input_file:
    positions = list(map(int, re.findall(("\d+"), input_file.read())))

length = len(positions)
small = positions[0]
big = positions[0]

for i in range(length):
    if positions[i] < small:
        small = positions[i]
    elif positions[i] > big:
        big = positions[i]

minfuel = 0

for i in range(small, big):
    fuel = 0
    for j in range(length):
        fuel += abs(positions[j] - i)
    if minfuel == 0:
        minfuel = fuel
    elif fuel < minfuel:
        minfuel = fuel

print(minfuel)
