# target area: x=60..94, y=-171..-136

answer = set()

for i in range(0, 100):
    for j in range(-200, 300):
        x_vel = i
        y_vel = j
        x = 0
        y = 0
        while y >= -171:
            x += x_vel
            y += y_vel
            if (60 <= x <= 94) and (-171 <= y <= -136):
                answer.add((i, j))
            else:
                y_vel -= 1
            if x_vel > 0:
                x_vel -= 1

print("Answer:", len(answer))
