import re

with open("input.txt") as input:
    diagnostics = list(map(str, re.findall(('\d+'), input.read())))

array_len = len(diagnostics)
item_len = len(diagnostics[0])

master = []

for i in range(item_len):
    master.append(0)

gamma_array, epsilon_array = '', ''

for i in range(array_len):
    for j in range(item_len):
        if diagnostics[i][j] == '1':
            master[j] += 1

for i in range(item_len):
    if master[i] > array_len/2:
        gamma_array += '1'
        epsilon_array += '0'
    else:
        epsilon_array += '1'
        gamma_array += '0'

gamma_rate, epsilon_rate = '', ''

for i in range(item_len):
    gamma_rate += gamma_array[i]
    epsilon_rate += epsilon_array[i]

print("Gamma rate: ", gamma_rate)
print("Gamma array: ", gamma_array)
print("Epsilon rate: ", epsilon_rate)

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

print("Power consumption: ", power_consumption)
