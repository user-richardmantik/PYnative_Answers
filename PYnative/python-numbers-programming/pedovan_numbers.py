COUNT_NUMS = 15

pedovan_nums = [1, 1, 1]

curr_p = 1
prev_p = 1
prev_prev_p = 1

for n in range(4, COUNT_NUMS + 1):
    next_p = prev_p + prev_prev_p

    pedovan_nums.append(next_p)

    prev_prev_p = prev_p
    prev_p = curr_p
    curr_p = next_p

print(pedovan_nums)