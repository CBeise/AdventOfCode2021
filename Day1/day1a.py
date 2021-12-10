import re

with open("adventinput.txt") as advent:
    depths = list(map(int, re.findall('\d+', advent.read())))

total = 0

for i in range(len(depths) - 1):
    if depths[i+1] > depths[i]:
        total += 1

print(total)
