def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
num_1 = 95
num_2 = 35

# prints 12
print ('The GCD of', num_1, 'and', num_2, 'is : ', gcd(num_1, num_2))