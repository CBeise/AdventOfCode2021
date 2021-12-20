import ast


with open("input.txt") as data_file:
    data = data_file.read().splitlines()

numbers = []

for item in data:
    row = ast.literal_eval(item)
    numbers.append(row)


def check_explosion(array):
    """This checks for any explosions"""
    punct = ['[', ']', ',', ' ']
    explosion = False
    line = str(array)
    counter = 0
    i = 0
    while i < len(line):
        if line[i] == '[':
            counter += 1
        elif line[i] == ']':
            counter -= 1

        if counter == 5:
            explosion = True
            left_i = i
            i += 1
            if '0' <= line[i + 1] <= '9':
                left = int(line[i: i + 2])
                i += 2
            else:
                if line[i] == "'":
                    print("X")
                left = int(line[i])
                i += 1
            while not ('0' <= line[i] <= '9'):
                i += 1
            if '0' <= line[i + 1] <= '9':
                right = int(line[i: i + 2])
                i += 2
            else:
                right = int(line[i])
                i += 1
            i += 1
            line = line[:left_i] + '0' + line[i:]
            i = left_i
            while i > 0:
                i -= 1
                if line[i] not in punct:
                    tweak = 0
                    if '0' <= line[i - 1] <= '9':
                        val = line[i-1:i+1]
                        tweak = -1
                    else:
                        val = line[i]
                    line = line[:i + tweak] + str(int(val) + left) + line[i + 1:]
                    i = 0
            i = left_i + 2
            while i < len(line):
                if line[i] not in punct:
                    num = 1
                    if '0' <= line[i + 1] <= '9':
                        val = line[i:i+2]
                        num = 2
                    else:
                        val = line[i]
                    line = line[:i] + str(int(val) + right) + line[i + num:]
                    i = len(line)
                i += 1
        i += 1

    if explosion:
        line = check_explosion(line)

    result = check_split(line)

    if result[0]:
        line = check_explosion(result[1])
    else:
        line = result[1]

    return line


def check_split(some_array, split=False):
    """This checks for a split"""
    for k in range(len(some_array)):
        if '0' <= some_array[k] <= '9':
            if '0' <= some_array[k + 1] <= '9':
                split = True
                val = int(some_array[k:k+2])
                some_array = some_array[:k] + '[' + str(int(val//2)) + ', ' + str(-int(-val//2)) + ']' + some_array[k+2:]
                return [split, some_array]

    return [split, some_array]


def calculate_magnitutde(homework):
    """This calculates the magnitude of the final answer"""
    total = 0
    if type(homework[0]) is list:
        total += calculate_magnitutde(homework[0]) * 3
    else:
        total += homework[0] * 3
    if type(homework[1]) is list:
        total += calculate_magnitutde(homework[1]) * 2
    else:
        total += homework[1] * 2

    return total


final = numbers[0]

for item in range(1, len(numbers)):
    final = check_explosion([final, numbers[item]])
    final = ast.literal_eval(final)

print(calculate_magnitutde(final))
