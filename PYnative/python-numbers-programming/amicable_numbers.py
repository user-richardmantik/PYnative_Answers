import math

def get_divisors_list(num):
    divisors_list = list()
    if (num != 1):
        for num_i in range (1, math.ceil(num/2)+1):
            if (num % num_i == 0):
                divisors_list.append(num_i)
    
    return divisors_list

def insert_sort(list, num):
    num_pos = 0
    if (len(list) > 0):
        while num_pos < len(list):
            if (num >= list[num_pos]):
                num_pos += 1
            else:
                break
    list.insert(num_pos, num)

sum_divisors_dict   = {}
start_num   = 0; end_num     = 76084
for num_i in range(start_num, end_num + 1):
    sum_divisors = math.floor(math.fsum(get_divisors_list(num_i)))
    if (sum_divisors not in sum_divisors_dict.keys()):
        sum_divisors_dict[sum_divisors] = list()
    sum_divisors_dict[sum_divisors].append(num_i)

for sum_divisors in sorted(sum_divisors_dict.keys()):
    for num_i in sum_divisors_dict[sum_divisors]:
        if (sum_divisors < num_i and num_i in sum_divisors_dict.keys() and sum_divisors in sum_divisors_dict[num_i]):
            print((sum_divisors, num_i))
