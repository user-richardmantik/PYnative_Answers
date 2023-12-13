import math

def is_mersenne(num):
    p = math.log2(num + 1)

    return math.floor(p) == math.ceil(p)

start_num   = 1
end_num     = 255
mersenne_numbers = []

for num_i in range(start_num, end_num + 1):
    if (is_mersenne(num_i)):
        mersenne_numbers.append(num_i)

print(mersenne_numbers)