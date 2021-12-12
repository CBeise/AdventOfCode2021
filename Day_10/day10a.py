with open("input.txt") as input_data:
    data = input_data.read().splitlines()

scores = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137}

total = 0

for i in range(len(data)):
    line = data[i]
    checker = []
    for index in range(len(line)):
        if line[index] == ")":
            if checker.pop() != "(":
                total += scores[")"]
                break
        elif line[index] == "]":
            if checker.pop() != "[":
                total += scores["]"]
                break
        elif line[index] == "}":
            if checker.pop() != "{":
                total += scores["}"]
                break
        elif line[index] == ">":
            if checker.pop() != "<":
                total += scores[">"]
                break
        else:
            checker.append(line[index])

print(total)
