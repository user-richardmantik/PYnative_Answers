input_num = 7536
print("Given number", input_num)
input_num_str = str(7536)
digits_list = list()
for digit in input_num_str:
    digits_list.insert(0, digit)
print(' '.join(digits_list))