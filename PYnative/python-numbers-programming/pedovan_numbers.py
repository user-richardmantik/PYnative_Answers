COUNT_NUMS = 15

pedovan_nums = [1, 1, 1]

curr_p = 1
last_p = 1
last_last_p = 1

for n in range(4, COUNT_NUMS + 1):
    next_p = last_p + last_last_p

    pedovan_nums.append(next_p)

    last_last_p = last_p
    last_p = curr_p
    curr_p = next_p

print(pedovan_nums)