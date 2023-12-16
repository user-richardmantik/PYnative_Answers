from itertools import combinations
 
comb = combinations(range(1, 45+1), 6)

count_combinations = len(list(comb))
print('count_combinations =', count_combinations)