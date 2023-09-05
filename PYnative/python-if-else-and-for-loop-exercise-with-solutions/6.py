num = 75869
curr_num = num
count_digits = 0
while (curr_num > 0):
    curr_num = curr_num // 10
    count_digits += 1
print('Total digits are:', count_digits)