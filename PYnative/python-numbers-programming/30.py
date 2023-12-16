start_num   = 100
end_num     = 999

three_digits_num_divisible_by_3_and_5   = []
for num_i in range(start_num, end_num + 1):
    if (num_i % 3 == 0 and num_i % 5 == 0):
        three_digits_num_divisible_by_3_and_5.append(num_i)

print(three_digits_num_divisible_by_3_and_5)
print('Count three_digits_num_divisible_by_3_and_5 =', len(three_digits_num_divisible_by_3_and_5))