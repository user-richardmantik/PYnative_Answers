import math

def get_divisors_list(num):
    divisors_list = list()
    if (num != 1):
        for num_i in range (1, math.ceil(num/2)+1):
            if (num % num_i == 0):
                divisors_list.append(num_i)
    
    return divisors_list

def aliquot_seq(n):
    curr_num = n

    aliquot_numbers = [curr_num]

    proper_divisors = get_divisors_list(curr_num)
    while (len(proper_divisors)) :
        sum_proper_divisors = int(math.fsum(proper_divisors))

        if (sum_proper_divisors == curr_num):
            aliquot_numbers.append(-1)
            break

        aliquot_numbers.append(sum_proper_divisors)

        proper_divisors = get_divisors_list(sum_proper_divisors)
        curr_num = sum_proper_divisors
    else:
        aliquot_numbers.append(0)

    return aliquot_numbers

input_num = int(input('Input:  n = '))
print('Output: ', end='')
aliquot_numbers = aliquot_seq(input_num)
if (aliquot_numbers[len(aliquot_numbers)-1] != -1):
    print(' '.join([str(num) for num in aliquot_numbers]))
else:
    tail_aliquot_numbers = aliquot_numbers[0:-1]
    last_aliquot_num     = aliquot_numbers[-2]
    print(' '.join([str(num) for num in tail_aliquot_numbers]))
    print('        Repeats with', last_aliquot_num)