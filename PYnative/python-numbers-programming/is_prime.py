import time
import math

start_time = time.time()
num = 1029384567

def get_divisors_list(num):
    divisors_list = list()
    if (num != 1):
        for num_i in range (1, math.ceil(num/2)+1):
            if (num % num_i == 0):
                divisors_list.append(num_i)
    
    return divisors_list

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return num != 1 and True

print (num, 'is ' + ('NOT ' if (not is_prime(num)) else '') + 'a prime number')
if (not is_prime(num)):
    divisor_list = get_divisors_list(num)
    print ('divisors =', divisor_list)
    prime_divisor_list = []
    for num_i in divisor_list:
        if (is_prime(num_i)): prime_divisor_list.append(num_i)
    print ('prime_divisors =', prime_divisor_list)

end_time = time.time()
print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms")