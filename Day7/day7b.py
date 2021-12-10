from day7a import positions, big, small, length

minfuel = 0

for i in range(small, big):
    fuel = 0
    for j in range(length):
        distance = abs(positions[j] - i)
        for k in range(distance + 1):
            fuel += k
    if minfuel == 0:
        minfuel = fuel
    elif fuel < minfuel:
        minfuel = fuel

print(minfuel)
