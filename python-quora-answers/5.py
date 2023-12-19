from itertools import permutations 

perm = permutations(range(0, 9+1), 4) 

# Print the obtained permutations
four_digits_odd_nums                           = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    if (num >= 1000 and num % 2 == 1):
        four_digits_odd_nums.append(num)

print ('count_4_digits_odd_numbers =', len(four_digits_odd_nums))