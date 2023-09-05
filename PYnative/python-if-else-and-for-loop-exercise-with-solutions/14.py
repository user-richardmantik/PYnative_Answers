import math

num = int(input('Enter a number: '))
quotient = num
while(quotient > 0):
    remainder = quotient % 10
    
    quotient = math.floor(quotient/10)
    print(remainder, end='')
print()