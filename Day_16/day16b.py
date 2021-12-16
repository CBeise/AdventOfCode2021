import numpy

with open("input.txt") as data_file:
    data = data_file.read().splitlines()[0]

binary = ""

for i in range(len(data)):
    cur = bin(int(data[i], 16))[2:]
    while len(cur) < 4:
        cur = "0" + cur
    binary += cur


def uunpack(bi_num):
    if bi_num == "":
        return
    bi_version = bi_num[:3]
    d_version = int(bi_version, 2)

    bi_type_id = bi_num[3:6]
    d_type_id = int(bi_type_id, 2)

    bi_num = bi_num[6:]

    if d_type_id == 4:
        total = ""
        while bi_num[0] != '0':
            total += bi_num[1:5]
            bi_num = bi_num[5:]
        total += bi_num[1:5]
        bi_num = bi_num[5:]
        total = int(total, 2)
    else:
        length_type_id = bi_num[0]
        bi_num = bi_num[1:]
        if length_type_id == '0':
            bi_sub_length = bi_num[:15]
            bi_num = bi_num[15:]
            d_sub_length = int(bi_sub_length, 2)
            target = len(bi_num)
            answers = []
            while target - len(bi_num) != d_sub_length:
                response = uunpack(bi_num)
                bi_num = response[0]
                answers.append(response[1])
        else:
            sub_num = int(bi_num[:11], 2)
            bi_num = bi_num[11:]
            answers = []
            for sub in range(sub_num):
                response = uunpack(bi_num)
                bi_num = response[0]
                answers.append(response[1])
        if d_type_id == 0:
            total = sum(answers)
        elif d_type_id == 1:
            total = numpy.prod(answers)
        elif d_type_id == 2:
            total = sorted(answers)[0]
        elif d_type_id == 3:
            total = sorted(answers, reverse=True)[0]
        elif d_type_id == 5:
            if answers[0] > answers[1]:
                total = 1
            else:
                total = 0
        elif d_type_id == 6:
            if answers[0] < answers[1]:
                total = 1
            else:
                total = 0
        else:
            if answers[0] == answers[1]:
                total = 1
            else:
                total = 0
    result = [bi_num, total]
    return result

print(uunpack(binary)[1])
