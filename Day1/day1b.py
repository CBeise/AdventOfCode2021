from day1a import depths

total = 0

for i in range(len(depths) - 3):
    if depths[i] < depths[i+3]:
        total += 1

print(total)
