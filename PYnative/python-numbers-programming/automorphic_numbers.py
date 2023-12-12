import time

def automorphic_numbers(power):
    automorphic_numbers = list()

    top = 0
    n = 5
    base = 10
    k = 1
    for i in range(1, power+1):
        size = 2**i
        n = (3*n**2 - 2*n**3) % (base**size)
        for j in range(k, size+1):
            m5 = n % (base**j)
            m6 = base**j + 1 - m5
            _, middle, bigger  = sorted([top, m5, m6])
            if middle > top:
                automorphic_numbers.append(middle)
            automorphic_numbers.append(bigger)
            top = bigger
        k = size + 1

    return automorphic_numbers

start_time = time.time()
automorphic_numbers = automorphic_numbers(4)
print (', '.join([str(num) for num in automorphic_numbers]))
end_time = time.time()

print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms")

























def is_automorphic(num):
    last_digit  = num % 10

    if (last_digit >= 5 and last_digit <= 6 and num > 1):
        num_squared     = num ** 2
    
        return (num_squared - num) % (10 ** count_digits(num)) == 0
    elif (num <=1):
        return True
    else:
        return False

def count_digits(num): 
    return math.floor(math.log10(num)+1) 

start_num   = 0
end_num     = 87109376
