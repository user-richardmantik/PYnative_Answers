numbers = []
i = 0
while (i < 5):
    print('Enter number at location ', (i+1), ': ', sep='', end = '')
    num = float(input())
    numbers.append(num)
    i+=1

print('User List:', sep=' ', end = '')
print(numbers)