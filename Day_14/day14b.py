with open("input.txt") as data_file:
    data = data_file.read().splitlines()

main_alphabet = {}


def count_letters(poly_string):
    alphabet = {}
    for letter in range(len(poly_string)):
        if poly_string[letter] in alphabet:
            alphabet[poly_string[letter]] += 1
        else:
            alphabet[poly_string[letter]] = 1
    return alphabet


def add_alphabet(alpha):
    for key in alpha:
        if key in main_alphabet:
            main_alphabet[key] += alpha[key]
        else:
            main_alphabet[key] = alpha[key]


polymer = data[0]

code = {}

for i in range(2, len(data)):
    item = data[i].split(" -> ")
    code[item[0]] = [item[1], item[0][0] + item[1] + item[0][1]]

for i in code:
    cur = i
    print(cur)
    for j in range(20):
        new_polymer = ""
        for k in range(len(cur) - 1):
            new_polymer += cur[k] + code[cur[k] + cur[k + 1]][0]
        new_polymer += cur[-1]
        cur = new_polymer
    code[i].append(cur)
    code[i].append(count_letters(cur))

for i in range(len(polymer) - 1):
    print(i)
    cur_poly = code[polymer[i:i+2]][2]
    for j in range(len(cur_poly) - 1):
        add_alphabet(code[cur_poly[j:j+2]][-1])
        main_alphabet[cur_poly[j + 1]] -= 1
main_alphabet[polymer[-1]] += 1

vals = sorted(main_alphabet.values())

print("Result: ", vals[-1] - vals[0])
