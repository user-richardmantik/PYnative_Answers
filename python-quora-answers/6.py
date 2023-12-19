from itertools import permutations 

perm = permutations([2, 3, 4, 7, 8], 3) 
 
# Print the obtained permutations
three_digits_nums                           = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    three_digits_nums.append(num)

three_digits_nums.sort()
print('count_three_digits_nums =', len(three_digits_nums))            