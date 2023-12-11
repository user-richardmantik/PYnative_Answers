import math

def is_harshad(num):
    num_str = str(num)
    sum_digits = math.fsum([int(n) for n in num_str])

    return num % sum_digits == 0

start_num   = 1
end_num     = 200

harshad_numbers = list()
for num_i in range(start_num, end_num + 1):
    if (is_harshad(num_i)):
        harshad_numbers.append(num_i)

print (', '.join([str(num) for num in harshad_numbers]))