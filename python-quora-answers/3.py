def is_requirements_met(num):
    num_str = str(num)
    is_hundreds_digit_twice_tens_digit = int(num_str[0]) == int(num_str[1]) * 2
    num_2_str = num_str[0] + num_str[2] + num_str[1]
    is_num_2_minus_num_1_equals_nine = int(num_2_str) - int(num_str) == 9
    return is_hundreds_digit_twice_tens_digit and is_num_2_minus_num_1_equals_nine

start_num   = 100
end_num     = 999

answers     = []
for num_i in range(start_num, end_num + 1):
    if (is_requirements_met(num_i)):
        answers.append(num_i)

print('Answers =', answers)