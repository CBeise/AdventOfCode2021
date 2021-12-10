from difflib import ndiff
from day8a import data


def string_sort(some_string):
    new_string = sorted(some_string)
    sorted_string = "".join(new_string)
    return sorted_string


total = 0

for i in range(len(data)):
    key = {}
    unused = []
    other_unused = []
    # Decipher the first half
    for j in data[i][0]:
        # Numbers 1, 4, 7, and 8 can be figured out by their length
        num = string_sort(j)
        if len(num) == 2:
            key[num] = 1
        elif len(num) == 3:
            key[num] = 7
            helper7 = num
        elif len(num) == 4:
            key[num] = 4
            helper4 = num
        elif len(num) == 7:
            key[num] = 8
            helper8 = num
        else:
            unused.append(num)
    for j in unused:
        # Number 9 has 6 edges and will contain every edge in the number 4
        if len(j) == 6 and all(elem in j for elem in helper4):
            key[j] = 9
        else:
            other_unused.append(j)
    unused = []
    for j in other_unused:
        # Number 0 has 6 edges and will contain every edge in the number 7
        if len(j) == 6 and all(elem in j for elem in helper7):
            key[j] = 0
        else:
            unused.append(j)
    other_unused = []
    for j in unused:
        # Number 3 has 5 edges and will contain every edge in the number 7
        if len(j) == 5 and all(elem in j for elem in helper7):
            key[j] = 3
        # The number 6 is the only remaining number with exactly 6 edges
        elif len(j) == 6:
            key[j] = 6
            helper6 = j
        else:
            other_unused.append(j)
    # Edge "E" is in the number 8 but not the number 6
    edge = [item[-1] for item in ndiff(helper8, helper6) if item[0] != ' ']
    for j in other_unused:
        # The number 2 contains edge "E"
        if all(elem in j for elem in edge):
            key[j] = 2
        # Now 5 is the only number left
        else:
            key[j] = 5

    # Decipher the second half
    value = ''
    for j in data[i][1]:
        num = string_sort(j)
        value += str(key[num])

    total += int(value)

print(total)
