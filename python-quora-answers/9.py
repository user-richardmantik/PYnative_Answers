from itertools import combinations
import numpy as np

comb = combinations([-2, 1, 3, -8, 5, 9, -9, 4, 7, -7, 8], 3)

max_product = 9*4*8
for tup in list(comb):
    product_of_tuple = np.prod(tup)
    if (product_of_tuple > max_product):
        max_product = product_of_tuple

print('max_product =', max_product)