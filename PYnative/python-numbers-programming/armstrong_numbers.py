import math

start_num = 1
end_num = 5000000

def get_digits(num):
    num_str = str(num)
    return [int(n) for n in num_str]

def count_digits(num): 
    return math.floor(math.log10(num)+1)

def sum_of_digits_to_the_power(num, pow):
    digits = get_digits(num)
    sum_of_digits_to_the_power = 0
    
    for digit in digits:
        sum_of_digits_to_the_power += digit ** pow
    
    return sum_of_digits_to_the_power

armsstrong_numbers = []
for num_i in range(start_num, end_num + 1):
    pow = count_digits(num_i)
    s = sum_of_digits_to_the_power(num_i, pow)
    if (s == num_i):
        armsstrong_numbers.append(num_i)

print(armsstrong_numbers)
    