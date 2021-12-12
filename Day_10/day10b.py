with open("input.txt") as input_data:
    data = input_data.read().splitlines()

incomplete = []

scores = {"(": 1,
          "[": 2,
          "{": 3,
          "<": 4}

for i in range(len(data)):
    line = data[i]
    checker = []
    for index in range(len(line)):
        if line[index] == ")":
            if checker.pop() != "(":
                break
        elif line[index] == "]":
            if checker.pop() != "[":
                break
        elif line[index] == "}":
            if checker.pop() != "{":
                break
        elif line[index] == ">":
            if checker.pop() != "<":
                break
        else:
            checker.append(line[index])
        if index == len(line) - 1:
            total = 0
            while len(checker) > 0:
                total *= 5
                total += scores[checker.pop()]
            incomplete.append(total)

incomplete.sort()

middle = (len(incomplete) // 2)

print(incomplete[middle])
