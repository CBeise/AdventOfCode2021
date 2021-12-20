import ast

from day18a import calculate_magnitutde, check_explosion, check_split, numbers

answers = []

for i in numbers:
    for j in numbers:
        if i != j:
            answers.append(calculate_magnitutde(ast.literal_eval(check_explosion([i, j]))))
            answers.append(calculate_magnitutde(ast.literal_eval(check_explosion([j, i]))))

print(sorted(answers)[-1])
