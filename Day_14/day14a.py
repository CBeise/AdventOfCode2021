with open("input.txt") as data_file:
    data = data_file.read().splitlines()

polymer = data[0]

code = {}

for i in range(2, len(data)):
    item = data[i].split(" -> ")
    code[item[0]] = item[1]

for i in range(10):
    new_polymer = ""
    for j in range(len(polymer) - 1):
        new_polymer += polymer[j] + code[polymer[j] + polymer[j + 1]]
    new_polymer += polymer[-1]
    polymer = new_polymer

alphabet = {}

for i in range(len(polymer)):
    if polymer[i] in alphabet:
        alphabet[polymer[i]] += 1
    else:
        alphabet[polymer[i]] = 0

vals = sorted(alphabet.values())

print("Result: ", vals[-1] - vals[0])
