import math
from itertools import permutations

start_num = 1
end_num = 3779

def count_digits(num): 
    return math.floor(math.log10(num)+1)

def get_cyclic_permutations(N):
    cyclic_permutations = []
    num = N
    n = count_digits(N)
    while (1):
        cyclic_permutations.append(int(num))
         
        rem = num % 10
        div = math.floor(num / 10)
        num = ((math.pow(10, n - 1)) * rem + div)
         
        if (num == N):
            break

    return cyclic_permutations

def get_is_prime_dict(start_num, end_num):
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

def is_circular_prime(num, is_prime_dict):
    numbers = get_cyclic_permutations(num)
    
    if (num != min(numbers)):
        return False
    
    if (num == 11116):
        print(num)
        print (min(numbers))

    is_circular_prime = True
    for num_i in numbers:
        if (num_i not in is_prime_dict.keys()):
            print (num, 'blah')

        if (not is_prime_dict[num_i]):
            is_circular_prime = False

    return is_circular_prime

is_prime_dict = get_is_prime_dict(start_num, int(len(str(end_num)) * '9'))
for num_i in range(start_num, end_num + 1):
    if (is_circular_prime(num_i, is_prime_dict)): 
        print(num_i)
