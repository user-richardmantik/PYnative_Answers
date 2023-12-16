from itertools import permutations 
 
# Get all permutations of [1, 2, 3] 
perm_1 = permutations([2, 3, 4, 5], 3)
perm_2 = permutations([2, 3, 4, 5], 4)
edward_nums = []
for t in list(perm_1): 
    num = int(''.join([str(d) for d in t]))
    if (num > 500):
        edward_nums.append(num)

for t in list(perm_2): 
    num = int(''.join([str(d) for d in t]))
    edward_nums.append(num)

print(edward_nums)
print('count_edward_nums =', len(edward_nums))