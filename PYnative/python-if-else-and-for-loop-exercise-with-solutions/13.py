def fectorial(num):
    if (num < 0):
        return None
    elif (num == 0):
        return 1
    else:
        ret_val = 1; 

        for i in range (0, num):
            ret_val *= (i+1)
        return ret_val

num = int(input('Enter a number: '))
f = fectorial(num)
if (f != None):
    print ('The factorial of', num, 'is', f)
else:
    print('5Factorial does not exist for negative numbers')