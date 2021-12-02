from day2a import distance

horizontal = 0
vertical = 0
aim = 0

for i in range(len(distance)):
    if distance[i][0] == "forward":
        horizontal += int(distance[i][1])
        vertical += aim * int(distance[i][1])
    elif distance[i][0] == "up":
        aim -= int(distance[i][1])
    else:
        aim += int(distance[i][1])

print("Horizontal: ", horizontal, "Vertical: ", vertical)
print("H * V: ", horizontal * vertical)
