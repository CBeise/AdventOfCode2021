import re

content = open("input.txt").readlines()

horizontal = 0
vertical = 0

with open("input.txt") as advent:
    distance = list(re.findall('(\w+) (\d+)', advent.read()))

for i in range(len(distance)):
    if distance[i][0] == "forward":
        horizontal += int(distance[i][1])
    elif distance[i][0] == "up":
        vertical -= int(distance[i][1])
    else:
        vertical += int(distance[i][1])

print("Horizontal: ", horizontal, "Vertical: ", vertical)
print("H * V: ", horizontal * vertical)
