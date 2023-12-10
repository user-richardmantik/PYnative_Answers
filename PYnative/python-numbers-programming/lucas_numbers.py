count_lucas_numbers = 10

num_1 = 2
num_2 = 1
temp = None
if (count_lucas_numbers > 1):
    print('First', count_lucas_numbers, 'Lucas numbers: ') 
    print (num_1)
    print (num_2)
    i = 2
    while (i < count_lucas_numbers):
        temp = num_2
        num_2 += num_1
        num_1 = temp

        print(num_2)

        i+=1

elif (count_lucas_numbers == 1):
    print('First 1 Lucas number: ') 
    print (1)
else:
    print (None)