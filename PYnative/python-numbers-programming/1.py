from itertools import permutations 
 
 
# Get all permutations of [1, 2, 3] 
perm = permutations([0, 1, 2, 3, 4, 5, 6], 3) 
 
# Print the obtained permutations
three_digits_nums                           = []
odd_three_digits_nums                       = []
count_greater_than_330_three_digits_nums    = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    if (num > 100):
        three_digits_nums.append(num)
        if (num % 2 == 1):
            odd_three_digits_nums.append(num)
        if (num > 330):
            count_greater_than_330_three_digits_nums.append(num)

print('count three_digits_nums =', len(three_digits_nums))
print('count_odd_three_digits_nums = ', len(odd_three_digits_nums))
print('count_greater_than_330_three_digits_nums', len(count_greater_than_330_three_digits_nums))