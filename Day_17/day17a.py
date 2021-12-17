# target area: x=60..94, y=-171..-136

answer = 0

for i in range(11, 14):
    for j in range(0, 171):
        x_vel = i
        y_vel = j
        x = 0
        y = 0
        y_max = 0
        while y >= -171:
            x += x_vel
            y += y_vel
            if y_vel > 0:
                y_max += y_vel
            if (60 <= x <= 94) and (-171 <= y <= -136):
                if y_max > answer:
                    answer = y_max
            else:
                y_vel -= 1
            if x_vel > 0:
                x_vel -= 1

print("Max height:", answer)
