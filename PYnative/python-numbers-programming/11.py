from itertools import permutations

perm = permutations([2,3,5,6,7,9], 3)
three_digits_nums    = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    if (num >= 100 and num % 5 == 0):
        three_digits_nums.append(num)

print (three_digits_nums)
print ('count_three_digits_nums =', len(three_digits_nums))