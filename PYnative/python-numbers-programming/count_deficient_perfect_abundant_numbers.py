import math

def get_divisors_list(num):
    divisors_list = list()

    if (num != 1):
        for num_i in range (1, math.ceil(num/2)+1):
            if (num % num_i == 0):
                divisors_list.append(num_i)
    
    return divisors_list

start_num   = 1
end_num     = 10000

count_deficient_num = count_perfect_num = count_abundant_num = 0
for num_i in range (start_num, end_num+1):
    sum_divisors = math.fsum(get_divisors_list(num_i))
    if (sum_divisors < num_i):
        count_deficient_num += 1
    elif (sum_divisors == num_i):
        count_perfect_num += 1
    else:
        count_abundant_num += 1

print('Number Counting [(integers) between {0} to {1:,}]: '.format(start_num, end_num))
print('Deficient number:', count_deficient_num)
print('Perfect number:', count_perfect_num)
print('Abundant number:', count_abundant_num)