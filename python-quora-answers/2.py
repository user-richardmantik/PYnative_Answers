from itertools import permutations 
 
def is_each_digits_not_in(num_1, num_2):
    num_1_str = [d for d in str(num_1)]
    num_2_str = [d for d in str(num_2)]
    is_each_digits_not_in = True
    for d in num_1_str:
        if (d in num_2_str):
            is_each_digits_not_in = False

    return is_each_digits_not_in


# Get all permutations of [1, 2, 3] 
perm = permutations([0, 1, 2, 3, 4, 5, 6], 3) 
 
# Print the obtained permutations
three_digits_nums                           = []
for t in list(perm): 
    num = int(''.join([str(d) for d in t]))
    if (num > 100):
        three_digits_nums.append(num)

three_digits_nums.sort()
max_sum = -1
for num_i in three_digits_nums:
    for num_j in three_digits_nums:
        if (is_each_digits_not_in(num_i, num_j) 
            and is_each_digits_not_in(num_j, num_i) 
            and (num_i + num_j) > max_sum):
            max_sum = num_i + num_j

print('Max Sum =', max_sum)
            