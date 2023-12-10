import math

start_num = 1
end_num = 1000

def is_kaprekar(num):
    num_squared_str = str(num**2)
    if (len(num_squared_str) == 1):
        return int(num_squared_str) == num
    else:
        num_squared_part_1 = int(num_squared_str[0:math.floor(len(num_squared_str)/2)])
        num_squared_part_2 = int(num_squared_str[math.floor(len(num_squared_str)/2):])

        return num_squared_part_1 + num_squared_part_2 == num

for num_i in range (start_num, end_num + 1):
    if (is_kaprekar(num_i)):
        print(num_i)