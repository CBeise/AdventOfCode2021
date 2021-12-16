with open("input.txt") as data_file:
    data = data_file.read().splitlines()[0]

binary = ""


for i in range(len(data)):
    cur = bin(int(data[i], 16))[2:]
    while len(cur) < 4:
        cur = "0" + cur
    binary += cur


def uunpack(bi_num, total):
    if bi_num == "":
        return

    bi_version = bi_num[:3]
    d_version = int(bi_version, 2)
    total += d_version

    bi_type_id = bi_num[3:6]
    d_type_id = int(bi_type_id, 2)

    bi_num = bi_num[6:]

    if d_type_id == 4:
        while bi_num[0] != '0':
            bi_num = bi_num[5:]
        bi_num = bi_num[5:]
    else:
        length_type_id = bi_num[0]
        bi_num = bi_num[1:]
        if length_type_id == '0':
            bi_sub_length = bi_num[:15]
            bi_num = bi_num[15:]
            d_sub_length = int(bi_sub_length, 2)
            target = len(bi_num)
            while target - len(bi_num) != d_sub_length:
                response = uunpack(bi_num, total)
                bi_num, total = response[0], response[1]
        else:
            sub_num = int(bi_num[:11], 2)
            bi_num = bi_num[11:]
            for sub in range(sub_num):
                response = uunpack(bi_num, total)
                bi_num, total = response[0], response[1]
    result = [bi_num, total]
    return result

print(uunpack(binary, 0)[1])
