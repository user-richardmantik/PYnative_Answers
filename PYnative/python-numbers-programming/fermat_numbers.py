def ith_fermat_number(i):
    return 2 ** (2 ** i) + 1

COUNT_NUMS = 10
for i in range(0, COUNT_NUMS + 1):
    print(ith_fermat_number(i))