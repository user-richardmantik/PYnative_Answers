import time
import math

COUNT_NUMS = 20

def get_divisors_list(num):
    divisors_list = list()
    if (num != 1):
        for num_i in range (1, num+1):
            if (num % num_i == 0):
                divisors_list.append(num_i)
    return divisors_list

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return num != 1 and True

def get_prime_divisors_list(num):
    divisor_list = get_divisors_list(num)
    prime_divisor_list = []
    for num_i in divisor_list:
        if (is_prime(num_i)): prime_divisor_list.append(num_i)
    return prime_divisor_list

hamming_numbers = []; num_i = 1
while (len(hamming_numbers) < COUNT_NUMS):
    prime_divisors_list = get_prime_divisors_list(num_i)
    if (set(prime_divisors_list).issubset((2,3,5))):
        hamming_numbers.append(num_i);
    num_i += 1
print(hamming_numbers)