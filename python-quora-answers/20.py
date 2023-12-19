from itertools import permutations

perm = permutations([1, 2, 3, 4, 5, 6], 3)
three_digits_nums    = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    three_digits_nums.append(num)

print (three_digits_nums)
print ('count_three_digits_nums =', len(three_digits_nums))