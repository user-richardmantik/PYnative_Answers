import math

def is_cube(num):
    return math.pow(num, 1/3) ** 3 == num

num = int(input('Input a number: '))
if (is_cube(num)):
    print(num, 'is a cube.')
else:
    print(num, 'is NOT a cube.')