import time
import math

start_time = time.time()
start_num = 1
end_num = 10000000

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return num != 1 and True

def is_mersenne_prime(num):
    p = math.log2(num + 1)

    return math.floor(p) == math.ceil(p) and is_prime(p) and is_prime(num)

for num in range(start_num, end_num + 1):
    if (is_mersenne_prime(num)):
        print (num, 'is a Mersenne Prime number')

end_time = time.time()
print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms")