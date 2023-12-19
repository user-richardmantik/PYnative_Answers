import math

input_num = int(input('Input: '))

juggler_numbers = []
curr_num  = input_num
last_num  = None

while (last_num != curr_num):
    juggler_numbers.append(curr_num)
    last_num = curr_num
    if (last_num is not None and (last_num % 2 == 0)):
        curr_num = math.floor(math.sqrt(last_num))
    else:
        curr_num = math.floor(math.sqrt(last_num ** 3))
    
print('Output:', ', '.join([str(num) for num in juggler_numbers]))