import math

start_num = 1
end_num = 200000

def get_digits(num):
    num_str = str(num)
    return [int(n) for n in num_str]

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

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return num != 1 and True

def has_digits_other_than_1_3_7_or_9(num):
    digits = get_digits(num)
    if (0 in digits or 2 in digits or 4 in digits or 5 in digits or 6 in digits or 8 in digits):
        return True
    else:
        return False
    
def is_circular_prime(num):
    if (num < 10) :
        return is_prime(num)
    elif (has_digits_other_than_1_3_7_or_9(num)):
        return False
    else:
        numbers = get_cyclic_permutations(num)

        if (num != min(numbers)):
            return False
        
        is_circular_prime = True
        for num_i in numbers:
            if (not is_prime(num_i)):
                is_circular_prime = False

        return is_circular_prime
    
circular_primes = []
for num_i in range(start_num, end_num + 1):
    if (is_circular_prime(num_i)): 
        circular_primes.append(num_i)

print(circular_primes)