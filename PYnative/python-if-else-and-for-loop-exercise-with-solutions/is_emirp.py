import math

def is_palindrome_number(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if (num_str[i] == num_str[0-(i+1)]):
            continue
        else:
            return False
        
    return True

def is_prime(num):
    for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
        if (num % num_1 == 0):
            return False
    return num != 1 and True

def reversed_number(num):
    if num < 0: return None;

    num_str = str(num)
    reversed_num_str = reversed(num_str)
    reversed_num = int(''.join(reversed_num_str))

    return reversed_num

start_num   = 100000
end_num     = 999999
for num in range(start_num, end_num + 1):
    reversed_num = reversed_number(num)
    if (not is_palindrome_number(num) and is_prime(num) and is_prime(reversed_num)):
        print(num, 'and', reversed_num, 'are prime numbers.')