import math

def create_is_prime_dict(num):
    start_num   = 1
    end_num     = num

    is_prime_dict = {}
    is_prime_dict[0] = False
    is_prime_dict[1] = False

    for i in range(1, end_num):
        num_i = i+1
        is_prime_dict[num_i] = True

    for num_i in range(2, math.ceil(end_num/2)):
        for num_j in range(num_i, math.ceil(end_num/2)):
            is_prime_dict[num_i * num_j] = False

    return is_prime_dict

def is_ugly_number(num):
    if (num == 1): return True
    
    is_prime_dict   = create_is_prime_dict(num)
    is_ugly_num     = (num % 2 == 0 or num % 3 == 0 or num % 5 == 0)
    for num_i in range (6, math.ceil(num/2) + 1):
        if (is_prime_dict[num_i] and num % num_i == 0):
            is_ugly_num     = False
    
    return is_ugly_num

input_num = int(input ('Input an integer number: '))
print (input_num, 'is ' + ('NOT ' if not is_ugly_number(input_num)else '') + 'an ugly number.')

start_num   = 1
end_num     = 15

print()
print('Ugly Numbers are:')
for num_i in range(start_num, end_num + 1):
    if (is_ugly_number(num_i)): print (num_i)