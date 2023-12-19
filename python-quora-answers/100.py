from itertools import permutations

perm = permutations([ 0, 1, 3, 4, 7, 9], 6)
# Print the obtained permutations
six_digits_nums = []
for t in list(perm):
    num = int(''.join([str(d) for d in t]))
    six_digits_nums.append(num)

six_digits_nums.sort()
print(six_digits_nums)