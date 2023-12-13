num_1 = 0
num_2 = 1
num_3 = 2

i = 0
COUNT_NUMS = 20

pell_numbers = []
while (i < COUNT_NUMS):
    temp    = num_2

    num_3   = num_2 * 2 + num_1
    num_2   = num_3
    num_1   = temp

    pell_numbers.append(str(num_1))
    
    i += 1

print(' '.join(pell_numbers))