import math

def factorial(num):
    if (num == 0 or num == 1): 
        return 1
    else:
        return  num * factorial(num-1)
    
def catalan_number(n):
    return math.floor(factorial(2 * n) / (factorial(n + 1) * factorial (n)))

start_n   = 0
end_n     = 11

for n in range (start_n, end_n + 1):
    print(catalan_number(n))