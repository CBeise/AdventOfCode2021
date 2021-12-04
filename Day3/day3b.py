from day3a import diagnostics, array_len, item_len, gamma_array

print('\nPart 2:\n')

print(array_len, item_len)

oxy_array, co2_array = [], []

cur_bit = 0

for i in range(array_len):
    if diagnostics[i][cur_bit] == gamma_array[cur_bit]:
        oxy_array.append(diagnostics[i])
    else:
        co2_array.append(diagnostics[i])

cur_bit += 1


while len(oxy_array) > 1:
    mcb = 0
    for i in range(len(oxy_array)):
        if oxy_array[i][cur_bit] == '1':
            mcb += 1
    done = False
    checker = 0
    if mcb >= len(oxy_array)/2:
        lcb = '0'
    else:
        lcb = '1'
    while not done:
        while not done and oxy_array[checker][cur_bit] == lcb:
            del(oxy_array[checker])
            if checker == len(oxy_array) or len(oxy_array) == 1:
                done = True
        checker += 1
        if checker >= len(oxy_array):
            done = True
    cur_bit += 1


print("Oxygen generator rating: ", oxy_array[0])

cur_bit = 1

while len(co2_array) > 1:
    mcb = 0
    for i in range(len(co2_array)):
        if co2_array[i][cur_bit] == '1':
            mcb += 1
    done = False
    checker = 0
    if mcb >= len(co2_array)/2:
        mcb = '1'
    else:
        mcb = '0'
    while not done:
        while not done and co2_array[checker][cur_bit] == mcb:
            del(co2_array[checker])
            if checker == len(co2_array) or len(co2_array) == 1:
                done = True
        checker += 1
        if checker >= len(co2_array):
            done = True
    cur_bit += 1

print("CO2 scrubber rating: ", co2_array[0])

oxy = int(oxy_array[0], 2)
co2 = int(co2_array[0], 2)

print("oxy: ", oxy)
print("co2: ", co2)

print("Life support rating: ", oxy * co2)
