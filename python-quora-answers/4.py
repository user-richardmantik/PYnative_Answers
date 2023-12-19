def is_requirements_met(num):
    num_str = str(num)
    is_product_two_digits_equals_24 = int(num_str[0]) * int(num_str[1]) == 24
    num_2_str = num_str[1] + num_str[0]
    is_num_2_minus_num_1_equals_18  = int(num_2_str) - int(num_str) == 18
    return is_product_two_digits_equals_24 and is_num_2_minus_num_1_equals_18

start_num = 10
end_num = 99
answers = []

for num_i in range(start_num, end_num + 1):
    if (is_requirements_met(num_i)):
        answers.append(num_i)

print('Answers =', answers)