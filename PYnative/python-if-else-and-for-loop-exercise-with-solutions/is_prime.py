import time
import math

start_time = time.time()
num = 116674323278833

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return True

print (num, 'is ' + ('NOT ' if (not is_prime(num)) else '') + 'a prime number')

end_time = time.time()
print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms")